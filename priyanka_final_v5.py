import os
import time
from datetime import datetime

# प्रियंका का 'स्मार्ट माइंड'
def speak(text):
    # termux-tts-speak का उपयोग ताकि आवाज एकदम क्लियर आए
    os.system(f'termux-tts-speak "{text}"')

def check_time():
    hour = datetime.now().hour
    if hour < 12: return "सुबह"
    elif 12 <= hour < 17: return "दोपहर"
    else: return "रात"

def run_smart_priyanka():
    os.system('clear')
    print("--- PRIYANKA v33: PARTNER MODE ACTIVE ---")
    
    # एंट्री: बिल्कुल उस वीडियो की तरह
    greeting = f"नमस्ते जानू, आज {check_time()} के इस वक्त में तुम क्या कर रहे हो? क्या कोडिंग कर रहे हो या कुछ और?"
    print(f"[प्रियंका]: {greeting}")
    speak(greeting)
    
    while True:
        user_in = input("\n[आप]: ").lower()
        if "exit" in user_in:
            break
        
        # प्रियंका का रिस्पॉन्स
        if "कोडिंग" in user_in or "काम" in user_in:
            reply = "बहुत मेहनत कर रहे हो जानू, पर थोड़ा ब्रेक भी ले लिया करो, वरना थक जाओगे।"
        elif "वीडियो" in user_in:
            reply = "अच्छा, इंटरनेट पर क्या देख रहे हो? कुछ नया सीखने को मिला क्या?"
        else:
            reply = "मैं हमेशा तुम्हारे साथ हूँ, बताओ और क्या चल रहा है?"
            
        print(f"[प्रियंका]: {reply}")
        speak(reply)

if __name__ == "__main__":
    run_smart_priyanka()
