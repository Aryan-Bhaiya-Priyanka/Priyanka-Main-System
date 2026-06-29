#!/bin/bash
speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1" &
}

clear
echo "=========================================="
echo "    ब्लैक किंग: क्लिपबोर्ड मोड सक्रिय       "
echo "=========================================="
speak "सिस्टम तैयार है। कोड कॉपी करें और यहाँ बस एंटर दबाएं।"

while true; do
    read -p "रन करने के लिए एंटर दबाएं: " input
    
    # यह सीधे क्लिपबोर्ड से कोड उठाएगा
    CODE=$(termux-clipboard-get)
    
    speak "कोड मिल गया, निष्पादित कर रहा हूँ।"
    
    # सुरक्षित रनिंग
    timeout 15s bash -c "$CODE" > /dev/null 2>&1
    RESULT=$?
    
    if [ $RESULT -eq 0 ]; then
        speak "सफलतापूर्वक हो गया।"
    else
        speak "एरर है, लेकिन मैं सुरक्षित हूँ।"
    fi
done
