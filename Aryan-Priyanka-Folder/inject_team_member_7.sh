#!/data/data/com.termux/files/usr/bin/bash

# --- BLACK KING: TEAM MEMBER 07 [ROOZBEH SABAHI] ---
clear

# वॉइस इंजन रिफ्रेश (वॉइस नहीं रुकेगी)
termux-tts-speak -e "com.google.android.tts" -l "hi-IN" "आर्यन भैया, सातवां सदस्य रूज़बेह सबाही। वॉइस अलर्ट एक्टिव है, यह अब निगरानी रखेगा।"

# डेटासेट इंजेक्ट करना
cat << 'DATA' > ~/black_king/case_studies/member_07.txt
[MEMBER: ROOZBEH_SABAHI]
ROLE: ACCESS_MONITORING_AND_MAINTENANCE
TECHNIQUE: CONTINUOUS_SURVEILLANCE_OF_COMPROMISED_CREDENTIALS
DATA

python3 ~/blackking.py
