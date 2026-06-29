import os

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_face_guardian():
    os.system('clear')
    print("--- PRIYANKA v36: FACE GUARDIAN ACTIVE ---")
    
    # प्रियंका का स्वागत और सुरक्षा का वादा
    speak("जानू, मैं तुम्हारी सुरक्षा के लिए तैयार हूँ। जब तक तुम नहीं आओगे, कोई छेड़छाड़ नहीं कर पाएगा।")
    
    while True:
        status = input("\n[सिस्टम]: क्या आप ही सामने हैं? (y/n): ")
        
        if status.lower() == 'y':
            speak("नमस्ते जानू, पहचान लिया। सिस्टम खोल रही हूँ।")
            print("[प्रियंका]: एक्सेस ग्रांटेड! स्वागत है।")
            break
        else:
            speak("नहीं, तुम मुझे धोखा नहीं दे सकते। यह लैपटॉप सुरक्षित है।")
            print("[प्रियंका]: एरर: अनाधिकृत पहुंच का प्रयास!")

if __name__ == "__main__":
    run_face_guardian()
