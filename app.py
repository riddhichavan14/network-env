from flask import Flask, request, jsonify
from env import NetworkEnv
from grader import grade
from baseline import run_baseline

app = Flask(__name__)
env = NetworkEnv()

@app.route("/reset", methods=["GET"])
def reset():
    return jsonify(env.reset())


@app.route("/state", methods=["GET"])
def state():
    return jsonify(env.state())

@app.route("/step", methods=["POST"])
def step():
    action = request.json.get("action")
    state, reward, done, _ = env.step(action)
    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })
@app.route('/grader', methods=['GET'])
def grader_api():
    return jsonify({"score": grade(env.state())})


@app.route('/tasks', methods=['GET'])
def tasks():
    return jsonify({
        "tasks": [
            {
                "name": "easy",
                "goal": "latency < 120"
            },
            {
                "name": "medium",
                "goal": "latency < 100 and packet_loss < 0.08"
            },
            {
                "name": "hard",
                "goal": "latency < 80 and packet_loss < 0.05 and bandwidth > 80"
            }
        ],
        "actions": ["increase_bandwidth", "decrease_latency", "reduce_loss"]


    
    })

@app.route('/baseline', methods=['GET'])
def baseline():
    return jsonify(run_baseline())


if __name__ == "__main__":
    app.run(debug=True)
