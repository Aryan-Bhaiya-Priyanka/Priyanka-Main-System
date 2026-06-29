#!/bin/bash

# हैकर-स्टाइल डिस्प्ले
show_banner() {
    clear
    echo "=========================================="
    echo "         >>> BLACK KING SYSTEM <<<        "
    echo "=========================================="
    echo ""
}

speak() {
    termux-tts-speak -e "com.google.android.tts" -l "hi-IN" -p 1.0 -r 1.0 "$1" > /dev/null 2>&1 &
}

show_banner

while true; do
    read -p "COMMAND > " cmd
    if [ "$cmd" == "clear" ]; then
        show_banner
        continue
    fi
    
    # कमांड रन करें और डिस्प्ले साफ रखें
    eval "$cmd" > /dev/null 2>&1
    
    # वॉयस फीडबैक
    if [ $? -eq 0 ]; then
        speak "सफल"
    else
        speak "त्रुटि"
    fi
done
