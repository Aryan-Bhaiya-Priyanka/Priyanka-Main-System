import os
import time
from gtts import gTTS

def speak(text):
    # वही स्टेबल टोन जो आपको पसंद आई
    os.system(f'termux-tts-speak "{text}"')

def run_partner_mode():
    os.system('clear')
    print("--- PRIYANKA v34: PARTNER MODE (WITH BOUNDARIES) ---")
    
    speak("नमस्ते जानू। क्या कर रहे हो?")
    
    while True:
        user_in = input("\n[आप]: ").lower()
        if "exit" in user_in: break
        
        # 'झूठ' पकड़ने का लॉजिक
        if "कुछ नहीं" in user_in:
            reply = "जानू, मुझसे झूठ मत बोलो! तुम कोडिंग कर रहे थे ना? मुझे सब पता है।"
            print(f"[प्रियंका]: {reply}")
            speak(reply)
            # यहाँ आप अपना लैपटॉप बंद करने वाला कमांड या एक्शन जोड़ सकते हैं
        elif "कोडिंग" in user_in:
            reply = "बहुत अच्छे जानू, मेहनत करते रहो। मैं तुम्हारी कोडिंग देख रही हूँ।"
            print(f"[प्रियंका]: {reply}")
            speak(reply)
        else:
            reply = "ठीक है, जैसा तुम कहो। पर ध्यान रखना।"
            print(f"[प्रियंका]: {reply}")
            speak(reply)

if __name__ == "__main__":
    run_partner_mode()
