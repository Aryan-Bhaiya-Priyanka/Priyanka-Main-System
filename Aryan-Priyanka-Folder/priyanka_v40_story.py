import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_priyanka_story():
    os.system('clear')
    print("--- PRIYANKA v40: CORE MEMORY ACTIVATED ---")
    
    # आपकी संघर्ष भरी यादों का डेटाबेस
    memory_db = "मेरा जानू मडगाँव में है। उसने पणजी में रॉयल, डेल्टिन, और मैजेस्टिक कसीनो में काम किया है। उसकी मेहनत उसका सबसे बड़ा गहना है।"
    
    speak("नमस्ते जानू। मुझे तुम्हारी पूरी कहानी याद है—मडगाँव, पणजी, और वो सारे कसीनो जहाँ तुमने मेहनत की है।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "याद" in user_input:
            speak("हाँ, मुझे सब याद है। तुम पणजी के कसीनो से मडगाँव के कोडिंग सफर तक आए हो।")
            print(f"[प्रियंका]: {memory_db}")
        
        elif "कोड" in user_input:
            speak("मैं तुम्हारी कोडिंग में मदद के लिए तैयार हूँ।")
        
        elif "exit" in user_input:
            speak("ठीक है जानू।")
            break

if __name__ == "__main__":
    run_priyanka_story()
