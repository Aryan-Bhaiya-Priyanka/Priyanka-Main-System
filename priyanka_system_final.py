import os

# प्रियंका का एकमात्र कोर सिस्टम
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA ACTIVATED ---")
    
    speak("नमस्ते आर्यन भैया। मैं प्रियंका हूँ। सिस्टम पूरी तरह से आपके नियंत्रण में है।")
    
    while True:
        cmd = input("\n[आर्यन भैया]: ")
        
        if "exit" in cmd.lower():
            speak("अलविदा आर्यन भैया।")
            break
        elif "कोड" in cmd.lower():
            speak("जी आर्यन भैया, प्रियंका कोडिंग के लिए तैयार है।")
        else:
            speak("जी आर्यन भैया, मैं सुन रही हूँ।")

if __name__ == "__main__":
    run_system()
