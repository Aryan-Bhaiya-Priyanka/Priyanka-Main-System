import os

# प्रिया का प्रियंका सिस्टम के साथ तालमेल
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA ACTIVATED ---")
    print("--- ASSISTANT: PRIYA READY ---")
    
    speak("नमस्ते आर्यन भैया। मैं प्रिया हूँ, आपकी साथी। प्रियंका सिस्टम पूरी तरह तैयार है।")
    
    while True:
        cmd = input("\n[आर्यन भैया]: ")
        
        if "exit" in cmd.lower():
            speak("अलविदा आर्यन भैया।")
            break
        elif "कोड" in cmd.lower():
            speak("जी आर्यन भैया, कोडिंग के लिए तैयार हूँ।")
        else:
            speak("जी आर्यन भैया, मैं सुन रही हूँ।")

if __name__ == "__main__":
    run_system()
