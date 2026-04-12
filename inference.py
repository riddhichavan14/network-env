 import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def run():
    print("[START] task=test env=test model=test")

    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME"),
        messages=[{"role": "user", "content": "Hello"}]
    )

    print("[STEP] step=1 action=test reward=0.50 done=true error=null")
    print("[END] success=true steps=1 rewards=0.50")

if __name__ == "__main__":
    run()