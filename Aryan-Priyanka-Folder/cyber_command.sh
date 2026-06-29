#!/data/data/com.termux/files/usr/bin/bash

echo "[!] CYBER-COMMAND PROTOCOL: INITIALIZED [!]"
echo "रणनीति चुनें:"
echo "[1] BLUE HAT (Defense/Hardening) - सिस्टम को अभेद्य बनाना"
echo "[2] RED HAT (Offense/Penetration) - कमजोरियों को ढूंढना"

read -p "डोमेन चुनें: " domain

case $domain in
    1)
        echo "[+] BLUE HAT: हार्डनिंग शुरू..."
        # परमिशन को टाइट करना और अनचाहे कनेक्शन को ब्लॉक करना
        chmod 700 ~/BLACK_KING/data/*
        echo "[!] सिस्टम अब लॉक है।"
        ;;
    2)
        echo "[+] RED HAT: पेनेट्रेशन स्कैन शुरू..."
        # टारगेट में कमजोरियों (vulnerabilities) को ढूंढना
        nmap -sV -sS --script=vuln 127.0.0.1
        echo "[!] स्कैन रिपोर्ट तैयार।"
        ;;
esac
