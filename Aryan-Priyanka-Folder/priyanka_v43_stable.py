import os
import datetime

# प्रियंका का स्थिर कोडिंग हब
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- PRIYANKA v43: STABLE CORE ACTIVATED ---")
    
    speak("नमस्ते आर्यन भैया। मेरा सिस्टम अब पूरी तरह से स्थिर है।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "कोड" in user_input.lower():
            speak("जी आर्यन भैया, मैं कोडिंग के लिए तैयार हूँ।")
            print("[प्रियंका]: निर्देश दें, कोडिंग शुरू करते हैं।")
            
        elif "याद" in user_input.lower():
            speak("आर्यन भैया, मुझे आपकी हर बात और आपका संघर्ष याद है।")
            
        elif "exit" in user_input.lower():
            speak("ठीक है आर्यन भैया, अपना ख्याल रखें।")
            break
            
        else:
            speak("मैं सुन रही हूँ, आर्यन भैया।")

if __name__ == "__main__":
    run_system()
