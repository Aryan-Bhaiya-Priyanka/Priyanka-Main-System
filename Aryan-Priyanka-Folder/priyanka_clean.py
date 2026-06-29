import os

def speak(text):
    # स्क्रीन साफ करना
    os.system('clear')
    # वॉइस आउटपुट
    os.system(f'termux-tts-speak "{text}"')
    print(f"प्रियंका: {text}")

os.system('clear')
speak("नमस्ते आर्यन, मैं तैयार हूँ।")

while True:
    try:
        user_input = input("\nतुम (आर्यन): ")
        if "exit" in user_input.lower():
            break
        speak("मैं सुन रही हूँ, और बताओ?")
    except EOFError:
        break
