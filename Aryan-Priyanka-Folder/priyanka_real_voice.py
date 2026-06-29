import os

# Google TTS के लिए जरूरी लाइब्रेरी इंस्टॉल करना
def install_requirements():
    os.system('pip install gTTS > /dev/null 2>&1')
    os.system('pkg install mpv -y > /dev/null 2>&1') # आवाज बजाने के लिए

def speak(text):
    # gTTS का उपयोग करके एकदम 'इंसानी' आवाज में बोलना
    from gtts import gTTS
    tts = gTTS(text=text, lang='hi', slow=False) # 'hi' मतलब हिंदी (इंडियन फीमेल)
    tts.save("response.mp3")
    os.system("mpv response.mp3 --no-video > /dev/null 2>&1")

def clear_screen():
    os.system('clear')

clear_screen()
install_requirements()
print("--- PRIYANKA v26: REAL INDIAN FEMALE VOICE ---")

welcome_msg = "नमस्ते। अब मैं बिल्कुल आपकी तरह और एकदम असली आवाज़ में बात करूँगी।"
print(f"[प्रियंका]: {welcome_msg}")
speak(welcome_msg)

while True:
    user_in = input("\n[आप]: ")
    if user_in.lower() == "exit":
        break
    
    response = "जी, मैं आपकी हर बात सुन रही हूँ।"
    print(f"[प्रियंका]: {response}")
    speak(response)
