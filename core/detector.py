# Detection logic using IOCs

def detect_threats(logs, malicious_ips, suspicious_files):
    alerts = []

    for log in logs:
        log = log.strip()

        # Check for malicious IPs
        for ip in malicious_ips:
            if ip in log:
                alerts.append(f"[IOC ALERT] Malicious IP detected: {ip}")

        # Check for suspicious files
        for file in suspicious_files:
            if file in log:
                alerts.append(f"[IOC ALERT] Suspicious file accessed: {file}")

    return alerts
