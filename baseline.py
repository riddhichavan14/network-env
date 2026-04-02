import requests

URL = "http://127.0.0.1:5000"

def run_baseline():
    requests.get(f"{URL}/reset")

    total_reward = 0

    for _ in range(20):
        action = "decrease_latency"
        res = requests.post(f"{URL}/step", json={"action": action}).json()
        total_reward += res["reward"]

        if res["done"]:
            break

    score = requests.get(f"{URL}/grader").json()
    return {"total_reward": total_reward, "score": score}

if __name__ == "__main__":
    print(run_baseline())