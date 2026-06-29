#!/data/data/com.termux/files/usr/bin/bash

# 1. सभी अटके हुए प्रोसेसेस को किल करें
pkill -f termux-tts-speak

# 2. स्क्रीन साफ़ करें
clear

# 3. बैनर दिखाएं
echo "=========================================="
echo "        [ BLACK KING SYSTEM ONLINE ]      "
echo "=========================================="

# 4. वॉइस कमांड को एक सेफ सब-शेल में चलाएं
(
  termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "सिस्टम रिसेट हो गया है, ब्लैक किंग तैयार है।"
) &

echo "[+] रिस्पॉन्स लूप ठीक कर दिया गया है।"
echo "[+] अब आप कमांड दे सकते हैं।"
