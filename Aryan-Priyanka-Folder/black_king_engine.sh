#!/bin/bash

# BLACK KING: GHOST MODE - HIGH SECURITY
# Status: Universal Execution & Voice Feedback Enabled

# हिंदी वॉयस फंक्शन
speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1"
}

run_universal() {
    local cmd="$1"
    speak "कोड निष्पादित हो रहा है"
    
    # टाइमआउट 30 सेकंड का है, ताकि लूप में न फंसे
    timeout 30s bash -c "$cmd" > /dev/null 2>&1
    
    local exit_code=$?
    if [ $exit_code -eq 124 ]; then
        speak "कोड बहुत समय ले रहा था, लूप से बाहर आ गया हूँ।"
    elif [ $exit_code -eq 0 ]; then
        speak "कोड सफलतापूर्वक चल गया।"
    else
        speak "कोड में त्रुटि आई, लेकिन सिस्टम सुरक्षित है।"
    fi
}

clear
echo "=========================================="
echo "      BLACK KING: GHOST MODE ACTIVE       "
echo "=========================================="
echo "Status: Execution Engine Ready"
echo "Voice: Hindi Feedback Active"
echo "------------------------------------------"
echo "उपयोग के लिए टाइप करें: run_universal 'आपका_कोड'"
