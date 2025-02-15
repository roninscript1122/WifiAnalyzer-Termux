# 📡 WifiAnalyzer-Termux

เครื่องมือสำหรับสแกนเครือข่าย Wi-Fi บนอุปกรณ์ Android ผ่าน Termux โดยใช้ `iwlist` และ `wireless-tools` เพื่อแสดงรายการเครือข่ายที่อยู่ใกล้เคียง พร้อมระดับสัญญาณ (dBm)

---

## 📥 วิธีติดตั้ง (Installation)

1. **อัปเดตและติดตั้งแพ็กเกจที่จำเป็น**
   ```sh
   pkg update && pkg upgrade -y
   pkg install git python wireless-tools -y
   ```
2. **Clone Repository จาก GitHub**
   ```sh
   git clone https://github.com/USERNAME/WifiAnalyzer-Termux.git
   cd WifiAnalyzer-Termux
   ```
3. **ให้สิทธิ์รันไฟล์**
   ```sh
   chmod +x wifi_analyzer.py
   ```

---

## 🚀 วิธีใช้งาน (How to Use)

1. **รันสคริปต์เพื่อสแกน Wi-Fi รอบตัวคุณ**
   ```sh
   python wifi_analyzer.py
   ```
2. **ระบบจะแสดงรายการเครือข่าย Wi-Fi ที่ตรวจพบ พร้อมค่าความแรงของสัญญาณ**

---

## 🛠️ คุณสมบัติ (Features)
✅ สแกนและแสดงรายการเครือข่าย Wi-Fi ใกล้เคียง
✅ แสดงค่าความแรงของสัญญาณ (dBm)
✅ ใช้งานง่ายผ่าน Termux บนอุปกรณ์ Android

---

## 📡 อุปกรณ์และระบบปฏิบัติการที่รองรับ (Supported Devices & OS)
- **📱 อุปกรณ์ที่รองรับ:** สมาร์ทโฟนและแท็บเล็ต Android ที่รองรับ Termux
- **💻 ระบบปฏิบัติการ:**
  - Android 7.0 ขึ้นไป (แนะนำให้ใช้กับ NetHunter หรืออุปกรณ์ที่รูทแล้วเพื่อประสิทธิภาพสูงสุด)

---

## 📌 เครดิต (Credits)
- **ผู้พัฒนา:** [RONIN Script](https://github.com/roninscript1122)
- **GitHub Repository:** [WifiAnalyzer-Termux](https://github.com/roninscript1122/WifiAnalyzer-Termux)

---

⚡ **หมายเหตุ:** โปรแกรมนี้ถูกพัฒนาสำหรับการศึกษาและทดลองเท่านั้น ห้ามใช้ในทางที่ผิดหรือกระทำการที่ผิดกฎหมาย!
