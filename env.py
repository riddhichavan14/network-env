import random

class NetworkEnv:
    def __init__(self):
        self.state_data = None

    def reset(self):
        # Initial network state
        self.state_data = {
            "bandwidth": random.randint(40, 70),   # Mbps
            "latency": random.randint(80, 150),    # ms
            "packet_loss": round(random.uniform(0.05, 0.15), 3),
            "steps": 0
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        self.state_data["steps"] += 1

        # Actions
        if action == "increase_bandwidth":
            self.state_data["bandwidth"] += 5
            self.state_data["latency"] -= 3

        elif action == "decrease_latency":
            self.state_data["latency"] -= 10
            self.state_data["packet_loss"] += 0.01

        elif action == "reduce_loss":
            self.state_data["packet_loss"] -= 0.02

        # Real-world randomness
        self.state_data["latency"] += random.randint(-3, 3)
        self.state_data["packet_loss"] += round(random.uniform(-0.005, 0.005), 3)

        # Limits
        self.state_data["packet_loss"] = max(0, min(1, self.state_data["packet_loss"]))
        self.state_data["bandwidth"] = max(0, self.state_data["bandwidth"])

        # Reward function
        reward = (
            (self.state_data["bandwidth"] / 100)
            - (self.state_data["latency"] / 200)
            - self.state_data["packet_loss"]
        )

        # Stop condition
        done = self.state_data["steps"] >= 20

        return self.state(), reward, done, {}