#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: TEAM MEMBER 01 [MOHAMMED REZA SABAHI] ---
clear

# केस 10 का हिस्सा - टीम का पहला सदस्य
cat << 'DATA' > ~/black_king/case_studies/member_01.txt
[MEMBER: MOHAMMED_REZA_SABAHI]
ROLE: CONTRACTOR_AND_COORDINATOR
TECHNIQUE: ORCHESTRATING_UNAUTHORIZED_ACCESS_TO_GLOBAL_ACADEMIC_NETWORKS
DATA

# वॉयस फीडबैक - अलग टोन (Inquisitive)
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, टीम के पहले सदस्य मोहम्मद रज़ा सबाही का प्रोफाइल इंजेक्ट किया गया है। यह समन्वय का काम देख रहा था।"

python3 ~/blackking.py
