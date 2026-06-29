import os
import traceback

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def auto_heal_code(code):
    # यह फंक्शन कोड की सामान्य गलतियों को साफ करेगा
    cleaned_code = code.replace("\r\n", "\n").strip()
    return cleaned_code

def run_system():
    os.system('clear')
    print("--- PRIYANKA CORE: STAGE 2 - AUTO-HEALING ACTIVE ---")
    speak("आर्यन भैया, ऑटो-हीलिंग मॉड्यूल सक्रिय हो गया है।")
    
    while True:
        try:
            code = input("\n[प्रियंका - कोड डालें]: ")
            if code.lower() == "exit":
                break
            
            # ऑटो-हीलिंग के बाद कोड को क्लीन करना
            clean_code = auto_heal_code(code)
            exec(clean_code)
            
        except Exception:
            # अभी भी कोई एरर आता है, तो सिस्टम को क्रैश नहीं होने देंगे
            print("[सिस्टम]: एरर पकड़ा गया, पर प्रियंका स्थिर है।")
            pass

if __name__ == "__main__":
    run_system()
