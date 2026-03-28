# 📦 Load IOC data (IPs and files)

def load_iocs():
    # Load malicious IPs
    with open("data/malicious_ips.txt", "r") as f:
        malicious_ips = [line.strip() for line in f]

    # Load suspicious files
    with open("data/suspicious_files.txt", "r") as f:
        suspicious_files = [line.strip() for line in f]

    return malicious_ips, suspicious_files
