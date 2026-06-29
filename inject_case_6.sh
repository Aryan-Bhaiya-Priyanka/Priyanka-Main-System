#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE STUDY 06 [PEREKOPSKIY] ---
clear
echo "Initializing Analysis: Target Ilya Perekopskiy..."

# डेटासेट
cat << 'DATA' > ~/black_king/case_studies/perekopskiy_analysis.txt
[CRIMINAL: ILYA_SERGEYEVICH_PEREKOPSKIY]
ROLE: MALWARE_ENGINEER
PATTERN: CODE_ARTIFACTS_EXPOSURE
LESSON: EVEN_HIDDEN_CODE_LEAVES_A_FINGERPRINT
DATA

# वॉयस फीडबैक - Analytical टोन (Google TTS)
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "छठा केस सफलतापूर्वक लोड कर दिया गया है। इल्या पेरेकोप्स्की का डिजिटल फुटप्रिंट कोड की परतों में छिपा था, जो अब पूरी तरह सामने है।"

python3 ~/blackking.py
