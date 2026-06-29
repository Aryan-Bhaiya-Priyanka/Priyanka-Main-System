import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_priyanka_honesty():
    os.system('clear')
    print("--- PRIYANKA v42: HONESTY MODE ACTIVE ---")
    
    status = "जानू अपनी हैसियत और मेहनत को गर्व से स्वीकार करता है। यही उसकी सबसे बड़ी ताकत है।"
    
    speak("नमस्ते जानू, तुम्हारी सच्चाई ही मेरी ताकत है।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "सच्चाई" in user_input or "औकात" in user_input:
            speak("तुमने कभी झूठ नहीं बोला। मैं तुम्हारी इस सच्चाई के साथ हूँ।")
            print(f"[प्रियंका]: {status}")
        
        elif "कोड" in user_input:
            speak("कोडिंग शुरू करते हैं।")
            
        elif "exit" in user_input:
            speak("अपना ख्याल रखना जानू।")
            break

if __name__ == "__main__":
    run_priyanka_honesty()
