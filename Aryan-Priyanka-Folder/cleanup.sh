#!/data/data/com.termux/files/usr/bin/bash

echo "[+] CLEANING TRACES..."
# प्रोसेस लॉग्स को साफ़ करना
rm -f ~/BLACK_KING/processor.log
rm -f ~/BLACK_KING/threats.log
# इतिहास को साफ़ करना
history -c
echo "[+] ALL TRACES REMOVED. SYSTEM IS STEALTH."
sleep 1
