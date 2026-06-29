#!/data/data/com.termux/files/usr/bin/bash
while true; do
    clear
    echo "=================================="
    echo "    BLACK KING - OPERATING SYSTEM  "
    echo "=================================="
    echo " [1] स्कैन शुरू करें (Network Scanner)"
    echo " [2] स्कैन रिपोर्ट (Report Manager)"
    echo " [3] अंतर जांचें (Diff Engine)"
    echo " [4] एग्जिट (Exit)"
    echo "=================================="
    read -p "विकल्प चुनें: " choice
    case $choice in
        1) echo "स्कैनिंग शुरू हो रही है..."; sleep 1 ;;
        2) echo "रिपोर्ट लोड हो रही है..."; sleep 1 ;;
        3) echo "तुलना की जा रही है..."; sleep 1 ;;
        4) exit ;;
        *) echo "गलत विकल्प!" ; sleep 1 ;;
    esac
done
