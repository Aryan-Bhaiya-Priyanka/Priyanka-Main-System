import os
import random
from gtts import gTTS

# प्रियंका की पूरी पर्सनालिटी और मूड्स
moods = {
    "happy": "आज तो बहुत काम निपटा लिया हमने! मैं बहुत खुश हूँ।",
    "calm": "सब ठीक हो जाएगा, बस शांति से काम करो।",
    "caring": "तुमने खाना खाया? तुम्हारी सेहत मेरे लिए कोडिंग से ज्यादा जरूरी है।"
}

def speak(text):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save("response.mp3")
    os.system("mpv response.mp3 --no-video > /dev/null 2>&1")

def run_priyanka():
    os.system('clear')
    print("--- PRIYANKA v30: MOOD ENGINE ACTIVE ---")
    
    welcome = "नमस्ते! मैं प्रियंका हूँ, आज हम किस मूड में काम करें?"
    print(f"[प्रियंका]: {welcome}")
    speak(welcome)
    
    while True:
        user_in = input("\n[आप]: ").lower()
        if "exit" in user_in:
            break
        
        # कीवर्ड के आधार पर मूड बदलना
        if "थकान" in user_in or "परेशान" in user_in:
            reply = moods["caring"]
        elif "काम" in user_in or "सफलता" in user_in:
            reply = moods["happy"]
        else:
            reply = moods["calm"]
            
        print(f"[प्रियंका]: {reply}")
        speak(reply)

if __name__ == "__main__":
    run_priyanka()
