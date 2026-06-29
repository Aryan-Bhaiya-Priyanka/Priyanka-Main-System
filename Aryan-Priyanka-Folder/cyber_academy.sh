#!/data/data/com.termux/files/usr/bin/bash

echo "[!] BLACK KING CYBER-ACADEMY: ENROLLMENT ACTIVE [!]"
echo "अपना लर्निंग पाथ चुनें:"
echo "[1] BASICS (Networking/OS) - नींव मजबूत करना"
echo "[2] FRAMEWORKS (NIST/Compliance) - मैनेजमेंट साइड"
echo "[3] OFFENSIVE (Pen-Testing) - Red Hat स्टाइल"

read -p "विकल्प चुनें: " option

case $option in
    1)
        echo "[+] मॉड्यूल 1: नेटवर्किंग और ओएस बेसिक्स..."
        echo "सीखें: TCP/IP, DNS, Linux Terminal, Hardware।"
        ;;
    2)
        echo "[+] मॉड्यूल 2: साइबर फ्रेमवर्क..."
        echo "सीखें: NIST CSF, रिस्क मैनेजमेंट, डिजिटल एसेट्स।"
        ;;
    3)
        echo "[+] मॉड्यूल 3: रेड टीम ऑपरेशन्स..."
        echo "सीखें: कमजोरियाँ ढूँढना, पेनेट्रेशन टेस्टिंग, डिफेंस इवेजन।"
        ;;
esac

echo "[!] निर्देश: अपनी प्रोग्रेस के लिए ~/BLACK_KING/progress_log.txt बनाएँ।"
