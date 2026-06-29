#!/bin/bash

# ब्लैक किंग: डायरेक्ट इनपुट मोड
speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1" &
}

clear
echo "=========================================="
echo "    ब्लैक किंग: डायरेक्ट रन मोड सक्रिय       "
echo "=========================================="
speak "सिस्टम तैयार है। सीधे कोड पेस्ट करें और एंटर दबाएं।"

while true; do
    # उपयोगकर्ता से सीधे इनपुट लें
    read -p "ब्लैक किंग > " user_cmd
    
    if [ "$user_cmd" == "exit" ]; then
        speak "सिस्टम बंद हो रहा है।"
        break
    fi

    speak "कोड रन कर रहा हूँ।"
    
    # सीधे कोड रन करें, टाइमआउट के साथ ताकि न फंसे
    timeout 15s bash -c "$user_cmd" > /dev/null 2>&1
    RESULT=$?
    
    if [ $RESULT -eq 124 ]; then
        speak "कोड लूप में फंस गया था, सुरक्षा के लिए रोक दिया।"
    elif [ $RESULT -eq 0 ]; then
        speak "कोड सफलतापूर्वक रन हुआ।"
    else
        speak "एरर आया, पर सिस्टम सुरक्षित है।"
    fi
done
