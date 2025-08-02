def predict_signal(row):
    import random
    return "BUY" if random.random() > 0.5 else "HOLD"