#!/data/data/com.termux/files/usr/bin/bash

echo "[!] MONARCH PROTOCOL INITIALIZED [!]"
echo "[1] IGRIS MODE (Stealth & Precision Strike)"
echo "[2] BERU MODE (Aggressive Brutal Force)"
echo "[3] BELLION MODE (Total Army Control)"
read -p "CHOOSE STYLE: " style

case $style in
    1)
        # IGRIS: बिना किसी फुटप्रिंट के निशाना साधो
        echo "[+] IGRIS STYLE: STEALTH MODE ENGAGED"
        bash ~/BLACK_KING/stealth_mode.sh
        ;;
    2)
        # BERU: सबसे कमजोर पॉइंट पर सीधा हमला
        echo "[+] BERU STYLE: AGGRESSIVE SCANNING"
        nmap -F 127.0.0.1 > ~/BLACK_KING/beru_target.txt
        echo "[+] TARGETS IDENTIFIED: READY FOR INJECTION"
        ;;
    3)
        # BELLION: पूरी सेना (स्क्रिप्ट्स) का एक साथ प्रहार
        echo "[+] BELLION STYLE: ORCHESTRATING ALL MODULES"
        bash ~/BLACK_KING/master_commander.sh
        ;;
    *) echo "INVALID STYLE" ;;
esac
