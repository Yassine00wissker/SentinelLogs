from collections import defaultdict
from statistics import mean

def build_baseline(metrics):
    """
    metrics = list of metric dicts
    each metric example:
    {
        "service": "auth-service",
        "logs_per_min": 12,
        "error_rate": 1.8,
        "timestamp": datetime
    }
    """
    grouped = defaultdict(list)

    for m in metrics:
        grouped[m["service"]].append(m)

    baselines = []

    for service,data in grouped.items():
        avg_logs = mean(d["logs_per_min"] for d in data)
        avg_errors = mean(d["error_rate"] for d in data)
        hours = sorted(set(d["timestamp"].hour for d in data))

        baselines.append({
            "service": service,
            "avg_logs_per_min": avg_logs,
            "avg_error_rate": avg_errors,
            "normal_hours": hours
        })
    return baselines