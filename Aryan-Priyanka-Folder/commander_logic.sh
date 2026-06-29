#!/data/data/com.termux/files/usr/bin/bash

echo "[!] MILITARY DOCTRINE INTEGRATED [!]"
echo "रणनीति का चयन करें:"
echo "[1] ARMY DOCTRINE (Frontline/Direct Assault - Brute Force)"
echo "[2] NAVY DOCTRINE (Strategic/Perks/Long-Range - Recon)"
echo "[3] AIR FORCE DOCTRINE (Technical/Advanced/Speed - Precision)"

read -p "डोमेन चुनें: " domain

case $domain in
    1) 
        echo "[+] ARMY MODE: डायरेक्ट हमला और फ्रंटलाइन डेटा प्रोसेसिंग।"
        # ये 'Beru' और 'Tank' की तरह काम करेगा।
        bash ~/BLACK_KING/processor_sync.sh
        ;;
    2) 
        echo "[+] NAVY MODE: लॉन्ग-रेंज डेटा रिकोनिसेंस (Recon)."
        # ये 'Igris' की तरह चुपचाप जानकारी जुटाएगा।
        bash ~/BLACK_KING/recon_bot.sh
        ;;
    3) 
        echo "[+] AIR FORCE MODE: टेक्निकल स्ट्राइक और स्टैल्थ।"
        # ये 'Kaisel' और 'Tusk' की तरह तेजी से काम करेगा।
        bash ~/BLACK_KING/stealth_mode.sh
        ;;
esac
