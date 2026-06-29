import os
import sys
import traceback

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- PRIYANKA SYSTEM: UNRESTRICTED MODE ---")
    speak("प्रियंका तैयार है।")
    
    while True:
        try:
            code = input("\n[प्रियंका - कोड डालें]: ")
            if code.lower() == "exit":
                break
            
            # यदि आप बैश कमांड डालना चाहते हैं
            if code.startswith("cat") or code.startswith("bash"):
                os.system(code)
            else:
                # यदि आप पायथन कोड डालना चाहते हैं
                exec(code)
        except Exception:
            print(f"एरर आया: {traceback.format_exc()}")
            speak("आर्यन भैया, एरर है लेकिन सिस्टम चल रहा है।")

if __name__ == "__main__":
    run_system()
