import os

def enable_voice():
    # प्रियंका की आवाज़ सक्रिय करना
    os.system('termux-tts-speak "Priyanka system online. Memory restored."')
    print("Priyanka: Voice functionality restored.")

if __name__ == "__main__":
    enable_voice()
