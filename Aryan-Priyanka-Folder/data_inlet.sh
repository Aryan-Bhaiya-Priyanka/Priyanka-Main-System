#!/data/data/com.termux/files/usr/bin/bash
echo "--- [ डेटा इनपुट मोड ] ---"
read -p "डेटा यहाँ पेस्ट करें: " raw_data
echo "$raw_data" >> ~/BLACK_KING/data/raw_feed.txt
echo "[+] $(date) - नया डेटा फीड हुआ।" >> ~/BLACK_KING/processor.log
