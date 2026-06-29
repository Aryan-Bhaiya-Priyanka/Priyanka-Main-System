import os

def speak(text):
    # वॉइस आउटपुट के लिए
    os.system(f'termux-tts-speak "{text}"')
    # डिस्प्ले के लिए
    print(f"प्रियंका: {text}")

print("--- प्रियंका सिस्टम एक्टिव (टेक्स्ट + वॉइस मोड) ---")
speak("नमस्ते आर्यन, मैं तैयार हूँ।")

while True:
    try:
        user_input = input("\nतुम (आर्यन): ")
        if user_input.lower() in ["exit", "bye", "बंद"]:
            speak("ठीक है, अपना ख्याल रखना।")
            break
        
        # यहाँ प्रियंका का रिस्पॉन्स
        response = "मैं सुन रही हूँ, और बताओ?"
        speak(response)
        
    except EOFError:
        break
