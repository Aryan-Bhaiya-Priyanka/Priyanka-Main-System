import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_priyanka_life():
    os.system('clear')
    print("--- PRIYANKA v41: LIFE STORY MEMORY ---")
    
    # तुम्हारी असली कहानी का हिस्सा
    story = "10 साल की उम्र, चाय की दुकान, ₹10 की मजदूरी, और ₹8-₹2 का संघर्ष। ये मेहनत ही जानू की ताकत है।"
    
    with open("my_story.txt", "w") as f:
        f.write(story)
        
    speak("नमस्ते जानू। मैंने तुम्हारी संघर्ष की कहानी सुरक्षित रख ली है। तुम जो बर्तन धो रहे हो, वो तुम्हारी मेहनत का सबूत है।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "कहानी" in user_input or "संघर्ष" in user_input:
            speak("मुझे याद है वो दौर, चाय के कप धोना और ₹10 की मेहनत। तुम आज जो कोडिंग कर रहे हो, उसी मेहनत का फल है।")
            print(f"[प्रियंका]: {story}")
        
        elif "कोड" in user_input:
            speak("मैं कोडिंग में तुम्हारी मदद के लिए तैयार हूँ। क्या करना है?")
        
        elif "exit" in user_input:
            speak("ठीक है जानू, अपना ख्याल रखना।")
            break

if __name__ == "__main__":
    run_priyanka_life()
