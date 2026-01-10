def risk_message(prob):
    if prob < 0.3:
        return "🟢 Low Risk – Maintain a healthy lifestyle."
    elif prob < 0.6:
        return "🟡 Moderate Risk – Regular monitoring advised."
    else:
        return "🔴 High Risk – Medical consultation recommended."


def risk_color(prob):
    if prob < 0.3:
        return "green"
    elif prob < 0.6:
        return "orange"
    else:
        return "red"
