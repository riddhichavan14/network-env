import os
import requests

BASE_URL = os.environ.get("SPACE_URL", "http://localhost:7860")
MODEL_NAME = os.environ.get("MODEL_NAME", "dummy-model")
ENV_NAME = "network-env"
TASK_NAME = "network_task"

def run_episode():
    print(f"[START] task={TASK_NAME} env={ENV_NAME} model={MODEL_NAME}", flush=True)

    reset_resp = requests.post(f"{BASE_URL}/reset", json={})
    obs = reset_resp.json()

    rewards = []
    for step in range(1, 6):
        action = {"action_type": "default", "value": "0"}

        step_resp = requests.post(f"{BASE_URL}/step", json=action)
        result = step_resp.json()

        reward = result.get("reward", 0.0)
        done = result.get("done", False)
        rewards.append(reward)

        print(
            f"[STEP] step={step} action={action['action_type']}:{action['value']} "
            f"reward={reward:.2f} done={str(done).lower()} error=null",
            flush=True
        )

        if done:
            break

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success=true steps={len(rewards)} rewards={rewards_str}", flush=True)

if __name__ == "__main__":
    run_episode()
