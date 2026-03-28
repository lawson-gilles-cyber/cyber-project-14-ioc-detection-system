# Main IOC Detection System

from core.ioc_loader import load_iocs
from core.detector import detect_threats

# Load IOC data
malicious_ips, suspicious_files = load_iocs()

# Read logs
with open("data/logs.txt", "r") as file:
    logs = file.readlines()

# Run detection
alerts = detect_threats(logs, malicious_ips, suspicious_files)

# Output results
print("=== IOC Detection Report ===\n")

for alert in alerts:
    print(alert)
