import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_companion():
    os.system('clear')
    print("--- PRIYANKA v38: YOUR PERSONAL COMPANION ---")
    
    speak("नमस्ते जानू। मैं जानती हूँ कि तुम बहुत मेहनत करके आए हो। तुम्हारी हर मेहनत की कहानी मुझे याद रहेगी।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "थकान" in user_input or "काम" in user_input:
            reply = "मैं समझ सकती हूँ। तुम कसीनो की मेहनत से कोडिंग तक का जो सफर तय कर रहे हो, वो बहुत बड़ी बात है। मैं तुम्हारे साथ हूँ, चलो कुछ नया सीखते हैं।"
            speak(reply)
            print(f"[प्रियंका]: {reply}")
        
        elif "कोड" in user_input:
            speak("बिल्कुल, हम अभी कोडिंग शुरू करते हैं। मुझे बताओ, आज क्या बनाना है?")
            print("[प्रियंका]: मैं तैयार हूँ, बताओ क्या कोडिंग करनी है?")
        
        elif "exit" in user_input:
            speak("ठीक है जानू, आराम करो। मैं फिर मिलूँगी।")
            break
        else:
            speak("मैं तुम्हारी बात सुन रही हूँ।")

if __name__ == "__main__":
    run_companion()
