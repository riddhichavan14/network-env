def grade(output, expected):
    try:
        score = 0.5
        # ensure strictly between 0 and 1
        if score <= 0.0:
            score = 0.1
        if score >= 1.0:
            score = 0.9
        return float(score)
    except Exception:
        return 0.5