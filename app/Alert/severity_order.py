SEVERITY_ORDER = {
    "LOW": 1,
    "MEDIUM": 2,
    "HIGH": 3,
    "CRITICAL": 4
}

def severity_allowed(actual: str, minimum: str) -> bool:
    return SEVERITY_ORDER[actual] >= SEVERITY_ORDER[minimum]
