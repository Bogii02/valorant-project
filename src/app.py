from flask import Flask, render_template

import data_manager

app = Flask(__name__)


@app.route('/')
def hello():
    agents = data_manager.get_agents()
    print(agents)
    return render_template('agents.html', agents=agents)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
