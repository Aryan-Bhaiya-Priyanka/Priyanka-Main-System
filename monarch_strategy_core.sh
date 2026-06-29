#!/data/data/com.termux/files/usr/bin/bash

echo "[!] MONARCH STRATEGY CORE INITIALIZED [!]"
echo "चुनें कि मिशन को कैसे अंजाम देना है:"
echo "------------------------------------------"
echo "[1] BELLION TACTICS: (अति-सुरक्षा और सर्वर कंट्रोल)"
echo "[2] BERU TACTICS: (तेज हमला और डेटा निचोड़ना)"
echo "[3] IGRIS TACTICS: (सटीकता और चुपके से ट्रैक करना)"
echo "[4] TUSK TACTICS: (मैजिक और भारी डेटा प्रोसेसिंग)"
echo "[5] KAMISH TACTICS: (डिस्ट्रक्शन और सबूत मिटाना)"
echo "------------------------------------------"

read -p "रणनीति चुनें: " tactic

case $tactic in
    1) echo "[+] BELLION PROTOCOL: सिस्टम की निगरानी शुरू..." ; ps aux ;;
    2) echo "[+] BERU PROTOCOL: डेटा का गहरा स्कैन शुरू..." ; grep -rnw ~/BLACK_KING/data/ ;;
    3) echo "[+] IGRIS PROTOCOL: टारगेट ट्रैकर्स तैनात..." ; nmap -T4 -F 127.0.0.1 ;;
    4) echo "[+] TUSK PROTOCOL: मास प्रोसेसिंग चालू..." ; tar -czf backup.tar.gz ~/BLACK_KING/data/ ;;
    5) echo "[+] KAMISH PROTOCOL: ट्रेसेस को जलाना (Wipe)..." ; rm -rf ~/BLACK_KING/temp/* ; history -c ;;
    *) echo "[-] गलत रणनीति!" ;;
esac
