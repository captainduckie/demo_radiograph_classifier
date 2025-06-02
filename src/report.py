def generate_report(preds, labels, threshold=0.5):
    report = "# AI Initial Assessment\n\n"
    systems = {
        "Respiratory": ["Effusion", "Infiltration"],
        "Cardiovascular": ["Cardiomegaly"],
    }

    for system, conditions in systems.items():
        report += f"## {system}\n"
        for i, cond in enumerate(conditions):
            if i >= len(preds):
                continue
            conf = preds[i]
            status = "✅" if conf > threshold else "❌"
            report += f"- {cond}: {status} ({conf:.2f})\n"
        report += "\n"

    alert = "⚠️ Moderate" if preds.max() > 0.7 else "✅ Low"
    report += f"Alert Level: {alert}\n"
    return report
