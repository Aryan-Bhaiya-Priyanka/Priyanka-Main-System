import os

# Google TTS Engine का उपयोग करने के लिए कमांड
def speak(text):
    print(f"प्रियंका: {text}")
    # --engine com.google.android.tts का उपयोग स्पष्ट आवाज़ के लिए
    os.system(f'termux-tts-speak --engine com.google.android.tts -l hi-IN "{text}"')

# पहली बार एक्टिवेशन
speak("नमस्ते आर्यन, मैं तैयार हूँ।")

while True:
    try:
        user_input = input("\nतुम (आर्यन): ")
        if user_input.lower() in ["exit", "bye", "बंद"]:
            speak("ठीक है, अपना ख्याल रखना।")
            break
        
        # यहाँ प्रियंका का रिस्पॉन्स
        speak("जी आर्यन, मैं सुन रही हूँ, और बताइए?")
        
    except EOFError:
        break
