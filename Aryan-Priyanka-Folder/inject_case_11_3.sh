#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: CASE 11 [IRGC CYBER ACTORS] - MEMBER 03 [BEHZAD MESRI] ---
clear

# वॉयस फीडबैक
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, तीसरा सदस्य बेहज़ाद मेसरी। डेटा चोरी और धमकी देने का इसका पैटर्न, अब ब्लैक किंग की मेमोरी में है।"

# डेटासेट इंजेक्ट करना
cat << 'DATA' > ~/black_king/case_studies/mesri_analysis.txt
[MEMBER: BEHZAD_MESRI]
ROLE: PENETRATION_TESTER_AND_EXTORTIONIST
PATTERN: DATA_THEFT_FOLLOWED_BY_PUBLIC_RELEASE_THREATS
LESSON: EXTORTION_LEAVES_TRACEABLE_DIGITAL_FOOTPRINTS
DATA

python3 ~/blackking.py
