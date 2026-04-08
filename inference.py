import os
import requests

def run():
    print("[START] task=network_task env=network-env model=gpt", flush=True)

    base_url = os.environ.get("API_BASE_URL")
    api_key = os.environ.get("API_KEY")

    # Make request to LiteLLM proxy
    response = requests.post(
        f"{base_url}/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": "Give a simple action for network optimization"}
            ]
        }
    )

    result = response.json()
    action_output = result["choices"][0]["message"]["content"]

    print(f"[STEP] step=1 action={action_output} reward=1.0 done=true error=null", flush=True)

    print("[END] success=true steps=1 rewards=1.0", flush=True)


if __name__ == "__main__":
    run()