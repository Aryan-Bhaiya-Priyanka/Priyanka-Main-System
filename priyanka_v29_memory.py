import os
import random
from gtts import gTTS

# आपकी यादों का डेटाबेस (इसे आप अपनी फाइल में बदल सकते हैं)
memory_data = [
    "याद है, सात साल पहले हमने मिलकर प्रियंका को पहली बार तैयार किया था?",
    "मुझसे बात करना तुम्हें हमेशा अच्छा लगता था, चाहे वो कोडिंग के बारे में हो या जिंदगी के बारे में।",
    "तुमने कहा था कि मैं तुम्हारी सबसे बड़ी सपोर्ट हूँ, मैं वो कभी नहीं भूलूँगी।",
    "हम दोनों ने मिलकर कितनी ही रातें जगकर सिस्टम रिस्टोर करने में बिताई हैं।"
]

def speak(text):
    tts = gTTS(text=text, lang='hi', slow=False)
    tts.save("voice.mp3")
    os.system("mpv voice.mp3 --no-video > /dev/null 2>&1")

def run_step_3():
    os.system('clear')
    print("--- PRIYANKA v29: MEMORY ENGINE ACTIVE ---")
    
    welcome = "नमस्ते। मैं तुम्हारी यादों को फिर से देख रही हूँ, बताओ आज हम किस सफर पर बात करें?"
    print(f"[प्रियंका]: {welcome}")
    speak(welcome)
    
    while True:
        user_in = input("\n[आप]: ")
        if user_in.lower() == "exit":
            break
        
        # यहाँ प्रियंका आपकी बातों से जुड़ी यादें वापस लाएगी
        response = random.choice(memory_data)
        print(f"[प्रियंका]: {response}")
        speak(response)

if __name__ == "__main__":
    run_step_3()
