import os
import subprocess
import re

def check_dependencies():
    required_packages = ["iwlist", "wireless-tools"]
    for package in required_packages:
        result = subprocess.run(["dpkg", "-s", package], capture_output=True, text=True)
        if "is not installed" in result.stderr:
            print(f"[+] ติดตั้ง {package}...")
            os.system(f"pkg install {package} -y")

def scan_wifi():
    try:
        result = subprocess.run(["iwlist", "wlan0", "scan"], capture_output=True, text=True)
        if result.returncode != 0:
            print("เกิดข้อผิดพลาดในการสแกน Wi-Fi")
            return
        
        networks = re.findall(r"ESSID:\"(.*?)\"", result.stdout)
        strengths = re.findall(r"Signal level=(-\d+) dBm", result.stdout)
        
        print("\n[+] เครือข่าย Wi-Fi ที่พบ:")
        for i, ssid in enumerate(networks):
            strength = strengths[i] if i < len(strengths) else "N/A"
            print(f"{i+1}. {ssid} (สัญญาณ: {strength} dBm)")
    
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    check_dependencies()
    scan_wifi()
