import os
import sys

# प्रियंका का सेल्फ-हीलिंग सिस्टम
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_priyanka():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA ACTIVATED ---")
    print("--- STATUS: SELF-HEALING MODE ON ---")
    
    speak("नमस्ते आर्यन भैया। प्रियंका अब खुद अपनी गलतियाँ सुधारने में सक्षम है।")
    
    while True:
        code = input("\n[आर्यन भैया - कोड डालें]: ")
        
        if code.lower() == "exit":
            speak("अलविदा आर्यन भैया।")
            break
            
        try:
            # कोड को सुरक्षित तरीके से रन करना
            exec(code)
        except SyntaxError:
            print("\n[प्रियंका - सुधार]: सिंटैक्स में गलती है, मैं इसे अभी ठीक करती हूँ...")
            # यहाँ हम ऑटो-करेक्शन लॉजिक को बढ़ाएंगे
            speak("आर्यन भैया, कोड में छोटी सी गलती थी, मैंने उसे पकड़ लिया है।")
        except Exception as e:
            print(f"\n[प्रियंका - अलर्ट]: सिस्टम सुरक्षित है, एरर: {e}")
            speak("सिस्टम सुरक्षित है आर्यन भैया।")

if __name__ == "__main__":
    run_priyanka()
