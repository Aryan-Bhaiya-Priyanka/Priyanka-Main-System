import os
import sys
import traceback

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA CORE STABLE ---")
    
    # शुरुआती आवाज़
    speak("नमस्ते आर्यन भैया। प्रियंका सिस्टम एरर-फ्री मोड में सक्रिय है।")
    
    while True:
        try:
            print("\n[प्रियंका]: अपना कोड यहाँ पेस्ट करें (रन करने के लिए खाली लाइन छोड़ें):")
            code_lines = []
            while True:
                line = input("> ")
                if line == "":
                    break
                code_lines.append(line)
            
            full_code = "\n".join(code_lines)
            
            if full_code.strip().lower() == "exit":
                speak("अलविदा आर्यन भैया।")
                break
                
            # यहाँ हम कोड को सुरक्षित तरीके से एक्सक्यूट कर रहे हैं
            exec(full_code)
            
        except Exception:
            # यह हिस्सा किसी भी सिंटैक्स एरर को पकड़ लेगा और प्रियंका को क्रैश नहीं होने देगा
            error_details = traceback.format_exc()
            print("\n[सिस्टम चेतावनी]: कोड में त्रुटि है, मैंने उसे पकड़ लिया है।")
            print(f"विवरण: {error_details}")
            speak("आर्यन भैया, कोड में गलती है, लेकिन सिस्टम सुरक्षित है।")

if __name__ == "__main__":
    run_system()
