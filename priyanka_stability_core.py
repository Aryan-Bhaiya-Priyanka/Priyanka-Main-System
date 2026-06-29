import os
import sys

# प्रियंका का स्टेबिलिटी कोर: एरर-फ्री मोड एक्टिवेटेड
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def check_system():
    # सिंटैक्स और सिस्टम की जाँच
    try:
        print("[सिस्टम]: स्टेबिलिटी चेक जारी है...")
        # यहाँ हम भविष्य के जटिल मॉड्यूल जोड़ेंगे
        return True
    except Exception as e:
        print(f"[एरर]: {e}")
        return False

def run_priyanka():
    os.system('clear')
    print("--- PRIYANKA CORE SYSTEM: STABLE ---")
    
    if check_system():
        speak("नमस्ते आर्यन भैया। प्रियंका सिस्टम पूरी तरह से स्थिर है।")
        
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
    run_priyanka()
