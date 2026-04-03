from flask import Flask, request, jsonify
from env import NetworkEnv
from grader import grade
from baseline import run_baseline

app = Flask(__name__)
env = NetworkEnv()

@app.route("/")
def home():
    return "API is running 🚀"

@app.route("/reset", methods=["GET", "POST"])
def reset():
    return jsonify(env.reset())

@app.route("/state", methods=["GET"])
def state():
    return jsonify(env.state())

@app.route("/step", methods=["POST"])
def step():
    data = request.get_json()
    action = data.get("action", 0)
    state, reward, done, _ = env.step(action)
    return jsonify({
        "state": state,
        "reward": reward,
        "done": done
    })

@app.route("/grader", methods=["GET"])
def grader_api():
    return jsonify({"score": grade(env.state())})

@app.route("/baseline", methods=["GET"])
def baseline():
    return jsonify(run_baseline())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
