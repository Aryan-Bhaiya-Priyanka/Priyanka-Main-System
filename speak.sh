#!/bin/bash
text="$1"
# Google TTS API को हिट करके आवाज़ डाउनलोड और प्ले करना
wget -q -U "Mozilla/5.0" "https://translate.google.com/translate_tts?ie=UTF-8&tl=hi&client=tw-ob&q=$text" -O /tmp/speech.mp3
play-audio /tmp/speech.mp3 > /dev/null 2>&1
