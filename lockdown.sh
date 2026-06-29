#!/data/data/com.termux/files/usr/bin/bash

echo "[!!!] WARNING: LOCKDOWN MODE ACTIVE [!!!]"
# गलत पासवर्ड या एक्सेस पर सिस्टम फ्रीज करना
read -s -p "ENTER SECURITY KEY: " key
if [ "$key" == "aryan123" ]; then
    echo "[+] ACCESS GRANTED."
else
    echo "[!] UNAUTHORIZED ACCESS! SYSTEM LOCKING..."
    sleep 2
    # यह स्क्रीन क्लियर करके वापस लॉक कर देगा
    clear
    exit
fi
