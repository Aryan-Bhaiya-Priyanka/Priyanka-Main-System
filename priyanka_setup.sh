# 1. आवश्यक पैकेज इंस्टॉल करें
pkg update -y
pkg install espeak -y

# 2. पायथन लाइब्रेरी इंस्टॉल करें
pip install pyttsx3

# 3. प्रियंका इंटरफ़ेस स्क्रिप्ट बनाएँ
cat << 'PYEOF' > priyanka.py
import os
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def start_priyanka():
    os.system('clear')
    print("========================================")
    print("        PRIYANKA AI - ACTIVE           ")
    print("========================================")
    msg = "नमस्ते, मैं प्रियंका हूँ। मैं तैयार हूँ।"
    print(msg)
    speak(msg)

if __name__ == "__main__":
    start_priyanka()
PYEOF

# 4. स्क्रिप्ट चलाएँ
python priyanka.py
