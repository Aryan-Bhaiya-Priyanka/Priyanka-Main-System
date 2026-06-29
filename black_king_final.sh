#!/bin/bash

# BLACK KING: GHOST MODE - HIGH SECURITY
# Status: FINAL STABLE BUILD (Error-Free & Loop-Proof)
# Voice: Hindi (Google Engine)

speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1" &
}

# सिस्टम को पूरी तरह से साफ रखें
clear
echo "=========================================="
echo "    BLACK KING: FINAL STABLE BUILD        "
echo "=========================================="
echo "Status: System Ready for Data Ingestion   "
echo "Voice: Hindi Feedback Enabled             "
echo "------------------------------------------"
speak "ब्लैक किंग मास्टर फाइनल बिल्ड तैयार है। मैं आपके कोड का इंतज़ार कर रहा हूँ।"

# लूप-फ्री प्रोसेसिंग इंजन
while true; do
    read -p "कोड इनपुट करें: " user_input
    
    if [ "$user_input" == "exit" ]; then
        speak "सिस्टम शटडाउन हो रहा है।"
        break
    fi

    # एरर-फ्री रनिंग
    timeout 60s bash -c "$user_input" > /dev/null 2>&1
    exit_status=$?

    if [ $exit_status -eq 124 ]; then
        speak "कोड लूप में फँस गया था, मैंने सुरक्षा के लिए इसे रोक दिया है।"
    elif [ $exit_status -eq 0 ]; then
        speak "कोड बिना किसी त्रुटि के सफल रहा।"
    else
        speak "कोड में त्रुटि आई, लेकिन सिस्टम बिल्कुल सुरक्षित है।"
    fi
done
