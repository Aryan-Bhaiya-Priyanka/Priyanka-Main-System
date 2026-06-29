import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def display_priyanka():
    os.system('clear')
    print("========================================")
    print("        PRIYANKA AI - INTERFACE         ")
    print("========================================")
    message = "नमस्ते, मैं प्रियंका हूँ। मैं आपकी सहायता के लिए तैयार हूँ।"
    print(message)
    speak(message)

if __name__ == "__main__":
    display_priyanka()
