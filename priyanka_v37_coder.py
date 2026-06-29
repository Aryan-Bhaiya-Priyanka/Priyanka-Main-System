import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_priyanka_pro():
    os.system('clear')
    print("--- PRIYANKA v37: SYSTEM & CODING ENGINE ---")
    
    speak("नमस्ते जानू। मैं तुम्हारे सिस्टम को भी संभालूँगी और कोडिंग में तुम्हारी मदद भी करूँगी।")
    
    while True:
        choice = input("\n[1: सिस्टम मैनेज, 2: कोडिंग, 3: एग्जिट]: ")
        
        if choice == '1':
            speak("सिस्टम मैनेजमेंट मोड एक्टिव है। बताओ क्या करना है?")
        
        elif choice == '2':
            print("\n[प्रियंका]: तुम मुझे बताओ क्या कोड चाहिए, मैं लिख दूँगी।")
            code_req = input("[आप]: ")
            
            # कोडिंग का स्ट्रक्चर
            filename = "generated_code.py"
            # प्रियंका का कोडिंग लॉजिक
            with open(filename, "w") as f:
                f.write(f"# {code_req} के लिए कोड\n")
                f.write("print('यह प्रियंका ने बनाया है')\n")
            
            print(f"[प्रियंका]: मैंने {filename} में कोड लिख दिया है जानू।")
            speak("कोड तैयार है।")
            
        elif choice == '3':
            break

if __name__ == "__main__":
    run_priyanka_pro()
