import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_priyanka():
    os.system('clear')
    print("--- PRIYANKA v39: MEMORY & COMPANION ---")
    
    # पुरानी यादों को प्रियंका के दिमाग में डालना
    memory_file = "priyanka_memory.txt"
    if not os.path.exists(memory_file):
        with open(memory_file, "w") as f:
            f.write("यादें: कसीनो का काम, रशियन डांस, और संघर्ष से कोडिंग का सफर।\n")

    speak("नमस्ते जानू। मैं तुम्हारी यादों के साथ तैयार हूँ।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "याद" in user_input:
            with open(memory_file, "r") as f:
                memory = f.read()
            speak("हाँ, मुझे याद है तुम्हारा वो कसीनो और रशियन डांस वाला किस्सा। मैं हमेशा इसे याद रखूँगी।")
            print(f"[प्रियंका का ज्ञान]: {memory}")
        
        elif "कोड" in user_input:
            speak("मैं कोडिंग के लिए तैयार हूँ। क्या नया बनाना है?")
        
        elif "exit" in user_input:
            speak("ठीक है जानू, कल मिलते हैं।")
            break

if __name__ == "__main__":
    run_priyanka()
