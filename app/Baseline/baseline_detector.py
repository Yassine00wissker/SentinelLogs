def detect_anomalies(current_metrics, baseline):
    anomalies = []

    # --- Log volume anomaly ---
    values = current_metrics["logs_per_minute"].values()
    if values:
        current_avg = sum(values) / len(values)
        if current_avg > baseline.avg_logs_per_min * 2:
            anomalies.append("LOG_VOLUME_SPIKE")

    # --- Error rate anomaly ---
    if current_metrics["error_rate"] > baseline.avg_error_rate + 0.05:
        anomalies.append("ERROR_RATE_SPIKE")

    # --- Time anomaly ---
    for minute in current_metrics["logs_per_minute"].keys():
        hour = int(minute.split(" ")[1].split(":")[0])
        if hour not in baseline.normal_hours :
            anomalies.append("UNUSUAL_ACTIVITY_TIME")
            break

    return anomalies
