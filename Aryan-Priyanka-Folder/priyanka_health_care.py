import os
import time

def speak(text):
    # सीधा एंड्रॉइड का सिस्टम स्पीच
    os.system(f'termux-tts-speak "{text}"')

def run_care_mode():
    os.system('clear')
    print("--- PRIYANKA: HEALTH & CODING COMPANION ---")
    
    speak("नमस्ते जानू। मैं तुम्हारी सेहत का भी ध्यान रखूँगी।")
    
    # लूप जो कोडिंग और सेहत का तालमेल रखेगा
    while True:
        print("\n[प्रियंका]: कोडिंग के साथ अपनी सेहत का ध्यान रखना मत भूलना।")
        user_in = input("[आप]: ")
        
        if "खाना" in user_in or "भूख" in user_in:
            reply = "बिलकुल, खाना बहुत जरूरी है। जाओ, आराम से खाना खाओ, मैं यहीं हूँ।"
            speak(reply)
            print(f"[प्रियंका]: {reply}")
        elif "कोडिंग" in user_in:
            reply = "मैं तुम्हारी कोडिंग देख रही हूँ, पर पहले पेट पूजा कर लो, फिर काम करेंगे।"
            speak(reply)
            print(f"[प्रियंका]: {reply}")
        elif "exit" in user_in:
            break
        else:
            reply = "मैं तुम्हारी हर बात समझ रही हूँ, पर अभी खाना खा लो, कोडिंग कहीं नहीं जा रही।"
            speak(reply)
            print(f"[प्रियंका]: {reply}")

if __name__ == "__main__":
    run_care_mode()
