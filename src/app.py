from flask import Flask, render_template, redirect, url_for, request

import data_manager
import populate_db

app = Flask(__name__)


@app.route('/')
@app.route('/agents', methods=['GET'])
def agents_route():
    agent_search = request.args.get('agent-search')

    if agent_search is not None:
        agent_search = agent_search.capitalize()
        agent = data_manager.get_agent_by_name(agent_search)
        if agent:
            return redirect(url_for('agent_details_route', agent_name=agent_search))
        else:
            return render_template('agents.html', agents=[])

    agents = data_manager.get_all_agents()
    if not agents:
        populate_db.save_agents(populate_db.get_agents())
        return redirect(url_for('agents_route'))

    return render_template('agents.html', agents=agents)


@app.route('/agents/<agent_name>', methods=['GET'])
def agent_details_route(agent_name):
    agent = data_manager.get_agent_by_name(agent_name)
    abilities = data_manager.get_abilities_by_agent(agent_name)
    return render_template('agent_details.html', agent=agent, abilities=abilities)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
