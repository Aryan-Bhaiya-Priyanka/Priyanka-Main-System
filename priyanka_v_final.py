import os
import sys

def speak(text):
    print(f"Priyanka: {text}")
    os.system(f'termux-tts-speak "{text}"')

speak("नमस्ते आर्यन, मैं एक्टिवेट हो गई हूँ। बताओ क्या सेवा करूँ?")

try:
    while True:
        # यह लाइन प्रॉम्प्ट देगी और इनपुट का इंतज़ार करेगी
        user_input = input("तुम्हारी बात: ")
        
        if "exit" in user_input.lower():
            speak("ठीक है, मैं जा रही हूँ।")
            break
        
        # यहाँ तुम्हारी प्रियंका का रिस्पॉन्स लॉजिक आएगा
        speak("मैं सुन रही हूँ, और बताओ?")
except KeyboardInterrupt:
    print("\nबंद कर रही हूँ...")
