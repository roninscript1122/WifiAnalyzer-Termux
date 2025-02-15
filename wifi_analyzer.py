import os
import subprocess
import re

def get_wifi_interface():
    result = subprocess.run(["iwconfig"], capture_output=True, text=True)
    interfaces = re.findall(r"(\w+)\s+IEEE 802.11", result.stdout)
    
    if interfaces:
        return interfaces[0]
    else:
        print("❌ ไม่พบอินเทอร์เฟซ Wi-Fi! ตรวจสอบว่าเปิด Wi-Fi แล้วหรือยัง")
        exit(1)

def check_dependencies():
    required_packages = ["wireless-tools"]
    
    for package in required_packages:
        result = subprocess.run(["dpkg", "-s", package], capture_output=True, text=True)
        if "is not installed" in result.stderr:
            print(f"[+] ติดตั้ง {package}...")
            os.system(f"sudo apt-get install {package} -y")

def scan_wifi(interface):
    try:
        result = subprocess.run(["sudo", "iwlist", interface, "scan"], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ เกิดข้อผิดพลาดในการสแกน Wi-Fi! โปรดตรวจสอบการตั้งค่าเครือข่าย")
            return
        
        networks = re.findall(r'ESSID:"(.*?)"', result.stdout)
        strengths = re.findall(r"Signal level=(-\d+) dBm", result.stdout)
        
        print("\n📡 เครือข่าย Wi-Fi ที่พบ:")
        if networks:
            for i, ssid in enumerate(networks):
                strength = strengths[i] if i < len(strengths) else "N/A"
                print(f"{i+1}. {ssid} (สัญญาณ: {strength} dBm)")
        else:
            print("🔍 ไม่พบเครือข่าย Wi-Fi")
    
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    check_dependencies()
    wifi_interface = get_wifi_interface()
    scan_wifi(wifi_interface)
