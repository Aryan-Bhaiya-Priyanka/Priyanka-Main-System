#!/data/data/com.termux/files/usr/bin/bash

echo "[!] MONARCH-TIER PROTOCOL ACTIVE [!]"
echo "चुनें कि मिशन का स्वरूप क्या है:"
echo "[S] KAISER/BIGROCK MODE (Max Damage & Crowd Clearing)"
echo "[A] BERU/IGRIS MODE (Critical Buffs & Precision)"
echo "[B/C] TANK/IRON MODE (Defense & Stun Support)"

read -p "टियर चुनें (S/A/B): " tier

case $tier in
    S)
        echo "[+] S-RANK MODE: ACTIVATING MAX DAMAGE OUTPUT..."
        # Kaisel/Bigrock का तरीका: पूरा डेटा एक साथ लोड और क्रश
        bash ~/BLACK_KING/data_inlet.sh && bash ~/BLACK_KING/processor_sync.sh
        ;;
    A)
        echo "[+] A-RANK MODE: ACTIVATING CRITICAL BUFFS..."
        # Beru/Igris का तरीका: सटीक टारगेट स्कैनिंग
        bash ~/BLACK_KING/recon_bot.sh && bash ~/BLACK_KING/stealth_mode.sh
        ;;
    B)
        echo "[+] B-RANK MODE: ACTIVATING STUN/DEFENSE PROTOCOL..."
        # Tank/Iron का तरीका: टारगेट को होल्ड करो और डिफेंस मजबूत करो
        bash ~/BLACK_KING/hunter_defense.sh
        ;;
    *) echo "[-] INVALID TIER. ABORTING." ;;
esac
