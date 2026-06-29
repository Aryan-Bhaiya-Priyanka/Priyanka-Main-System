#!/data/data/com.termux/files/usr/bin/bash

echo "[!!!] WARNING: KILL-SWITCH TRIGGERED [!!!]"
read -p "ARE YOU SURE? (y/n): " confirm
if [ "$confirm" == "y" ]; then
    echo "[+] WIPING ALL DATA..."
    # फोल्डर का नामोनिशान मिटाना
    rm -rf ~/BLACK_KING
    history -c
    echo "[+] SYSTEM WIPED. NO TRACES LEFT."
    exit
else
    echo "[+] ABORTED."
fi
