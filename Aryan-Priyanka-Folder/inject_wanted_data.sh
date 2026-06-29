#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: WANTED CINEMATIC DATA MODULE ---
clear
echo "[+] 'Wanted' नॉलेज डेटासेट इंजेक्ट हो रहा है..."
mkdir -p ~/black_king/data/wanted_movie
cd ~/black_king/data/wanted_movie

# फिल्म का स्ट्रैटेजिक डेटा (कर्व द बुलेट लॉजिक)
cat << 'DATA' > wanted_knowledge.txt
[MOVIE_DATA: WANTED]
STYLE: PRECISION_AGGRESSION
CORE_CONCEPT: CURVE_THE_BULLET_TRAJECTORY
STRATEGY: ELIMINATION_WITH_CALCULATED_PATH
SYSTEM_MODE: HIGH_SPEED_THREAT_RESPONSE
DATA

echo "[+] डेटा लेयर 'wanted_knowledge.txt' सफलतापूर्वक इंजेक्ट कर दी गई है।"
sleep 1

# वॉइस फीडबैक
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "वांटेड फिल्म का नॉलेज डेटा ब्लैक किंग में लोड हो गया है, सर।"

# --- मास्टर लिंक इंटीग्रेशन (जो आपने बताया था) ---
chmod +x ~/blackking.py
python3 ~/blackking.py
