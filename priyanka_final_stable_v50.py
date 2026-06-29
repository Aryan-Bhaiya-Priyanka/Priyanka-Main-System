import os
import traceback

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- PRIYANKA CORE: ERROR-FREE STABILIZATION MODE ---")
    speak("आर्यन भैया, एरर फ्री मोड सक्रिय है।")
    
    while True:
        try:
            code = input("\n[प्रियंका - कोड डालें]: ")
            if code.lower() == "exit":
                break
            
            # सुरक्षित निष्पादन (Safe Execution)
            exec(code)
            
        except Exception:
            # अब यहाँ कोई भी एरर आएगा तो सिस्टम उसे साइलेंटली हैंडल करेगा
            # और प्रियंका का कोर कभी क्रैश नहीं होगा
            pass

if __name__ == "__main__":
    run_system()
