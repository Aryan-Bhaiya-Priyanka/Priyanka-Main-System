#!/data/data/com.termux/files/usr/bin/bash

# GORILLA WARFARE: HIT AND RUN, STEALTH, SURPRISE
echo "[!] GORILLA WARFARE PROTOCOL: LETHAL STEALTH ACTIVATED [!]"

read -p "टारगेट (Target) का नाम/पाथ: " target_file

# 1. SURPRISE (टारगेट को घेरना)
echo "[*] SURPRISE ATTACK: टारगेट के इर्द-गिर्द घेराबंदी..."
ls -R | grep "$target_file" > ~/BLACK_KING/target_trace.txt

# 2. HIT (डेटा एक्सट्रैक्शन/स्ट्राइक)
echo "[!] HIT: टारगेट पर प्रहार..."
cat "$(cat ~/BLACK_KING/target_trace.txt)" > ~/BLACK_KING/extracted_data.tmp

# 3. RUN (गायब होना - Zero Trace)
echo "[*] VANISH: सबूत मिटाए जा रहे हैं..."
rm ~/BLACK_KING/target_trace.txt
history -d $(history | tail -n 2 | head -n 1 | awk '{print $1}')
echo "[!] मिशन पूरा हुआ। सिस्टम अब 'अदृश्य' है।"
