import os
import datetime

# प्रियंका का वॉइस-इनेबल्ड कोडिंग हब
def speak(text):
    # यह कमांड सुनिश्चित करती है कि वॉइस आउटपुट सही हो
    os.system(f'termux-tts-speak "{text}"')

def log_data(task):
    with open("priyanka_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {task}\n")

def run_priyanka():
    os.system('clear')
    print("--- PRIYANKA v44: SYSTEM STABLE ---")
    
    speak("नमस्ते आर्यन भैया। प्रिया, आपकी सेवा में हाजिर है। सिस्टम पूरी तरह से तैयार है।")
    
    while True:
        user_input = input("\n[आप]: ")
        
        if "exit" in user_input.lower():
            speak("ठीक है आर्यन भैया, फिर मिलेंगे।")
            break
        
        elif "कोड" in user_input.lower():
            speak("निर्देश दीजिए आर्यन भैया, मैं तैयार हूँ।")
            log_data("Coding session started")
            
        else:
            log_data(user_input)
            speak("मैंने नोट कर लिया है, आर्यन भैया।")

if __name__ == "__main__":
    run_priyanka()
