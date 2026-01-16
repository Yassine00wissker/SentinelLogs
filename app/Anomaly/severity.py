def calculate_severity(value: float, threshold: float) -> str:
    ratio = value / threshold

    if ratio >= 3:
        return "CRITICAL"
    elif ratio >= 2:
        return "HIGH"
    elif ratio >= 1.5:
        return "MEDIUM"
    else:
        return "LOW"