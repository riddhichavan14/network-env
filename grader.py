def grade(state):
    score = 0.0

    if state["latency"] < 100:
        score += 0.3

    if state["packet_loss"] < 0.05:
        score += 0.3

    if state["bandwidth"] > 75:
        score += 0.4

    return min(score, 1.0)