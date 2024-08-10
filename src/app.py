from flask import Flask, render_template, redirect, url_for, request, jsonify
import data_manager
import populate_db

app = Flask(__name__)


@app.route('/')
@app.route('/agents', methods=['GET'])
def agents_route():
    agent_search = request.args.get('agent-search')
    role_search = request.args.get('role-search')

    if agent_search:
        return redirect(url_for('agent_details_route', agent_name=agent_search))

    if role_search:
        return redirect(url_for('agents_by_role_route', role=role_search))

    agents = data_manager.get_all_agents()
    if not agents:
        populate_db.save_agents(populate_db.get_agents())
        return redirect(url_for('agents_route'))

    return render_template('agents.html', agents=agents, query='')


@app.route('/agents/<agent_name>', methods=['GET'])
def agent_details_route(agent_name):
    agent = data_manager.get_agent_by_name(agent_name)
    abilities = data_manager.get_abilities_by_agent(agent_name)
    return render_template('agent_details.html', agent=agent, abilities=abilities)


@app.route('/agents/role/<role>', methods=['GET'])
def agents_by_role_route(role):
    agents = data_manager.get_agents_by_role(role.capitalize())
    if not agents:
        return render_template('agents_list.html', agents=[], message=f"No agents found for the role '{role}'")
    return render_template('agents_list.html', agents=agents)


@app.route('/weapons', methods=['GET'])
def weapons_route():
    weapons = data_manager.get_all_weapons()
    if not weapons:
        populate_db.save_weapons(populate_db.get_weapons())
        return redirect(url_for('weapons_route'))
    return render_template('weapons.html', weapons=weapons)


@app.route('/weapon/skins/<weapon_name>', methods=['GET'])
def weapon_skins_route(weapon_name):
    skins = data_manager.get_skins_by_weapon(weapon_name)
    return render_template('weapon_skins.html', skins=skins)


@app.route('/maps', methods=['GET'])
def maps_route():
    maps = data_manager.get_all_maps()
    return render_template('maps.html', maps=maps)


@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = [agent[1] for agent in data_manager.get_all_agents() if query in agent[1].lower()]
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
