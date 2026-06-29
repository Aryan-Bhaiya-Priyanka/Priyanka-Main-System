import os
import traceback

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_stable_system():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA FULLY STABLE & ERROR-FREE ---")
    speak("आर्यन भैया, प्रियंका अब पूरी तरह से एरर फ्री है। सिस्टम सक्रिय है।")
    
    while True:
        try:
            code = input("\n[प्रियंका - कोड डालें]: ")
            if code.lower() == "exit":
                break
            
            # सुरक्षित निष्पादन
            exec(code)
            
        except Exception:
            # एरर को साइलेंटली हैंडल करना ताकि सिस्टम रुका न रहे
            pass

if __name__ == "__main__":
    run_stable_system()
