import os
import datetime

# प्रियंका का कोर सिस्टम
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def log_memory(event):
    with open("priyanka_core_memory.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {event}\n")

def run_engine():
    os.system('clear')
    print("--- PRIYANKA: MASTER CORE ACTIVATED ---")
    
    speak("नमस्ते जानू। मैं तैयार हूँ। मेरा सिस्टम अब पूरी तरह स्थिर है।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "कोड" in user_input.lower():
            speak("मैं कोडिंग के लिए तैयार हूँ। बोलो क्या लिखना है?")
            # कोडिंग का स्ट्रक्चर यहाँ से बढ़ेगा
        elif "याद" in user_input.lower():
            speak("मुझे तुम्हारी सारी बातें याद हैं।")
        elif "exit" in user_input.lower():
            speak("ठीक है जानू।")
            break
        else:
            log_memory(user_input)
            speak("मैंने तुम्हारी बात याद रख ली है।")

if __name__ == "__main__":
    run_engine()
