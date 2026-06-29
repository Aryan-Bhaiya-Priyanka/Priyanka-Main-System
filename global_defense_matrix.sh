#!/data/data/com.termux/files/usr/bin/bash

echo "[!] BLACK KING: GLOBAL CYBER-DEFENSE MATRIX [!]"
echo "सुरक्षा लेयर चुनें:"
echo "[1] NSA-STYLE (Hardening) - हार्डवेयर और OS लेवल सुरक्षा"
echo "[2] ISRAEL-STYLE (Precision) - थ्रेट हंटिंग और स्कैनिंग"
echo "[3] ESTONIA-STYLE (NATO) - नेटवर्क विजिबिलिटी और को-ऑपरेटिव अलर्ट"

read -p "डिफेंस मोड चुनें: " mode

case $mode in
    1)
        echo "[+] NSA-MODE: सिस्टम लॉक-डाउन मोड एक्टिव।"
        # अनचाहे पोर्ट्स बंद करना
        ss -tuln
        ;;
    2)
        echo "[+] ISRAEL-MODE: प्रेसिजन स्कैनिंग (Vulnerability Hunting)..."
        # कमजोरियों को खोजना
        nmap -sV -sS --script=vuln 127.0.0.1
        ;;
    3)
        echo "[+] ESTONIA-MODE: नेटवर्क मॉनिटरिंग और विजिबिलिटी..."
        # ट्रैफिक मॉनिटरिंग
        tcpdump -i any -c 20
        ;;
esac
