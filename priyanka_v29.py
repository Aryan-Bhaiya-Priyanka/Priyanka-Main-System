import os, random, threading, time, queue

voice_queue = queue.Queue()

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

threading.Thread(target=voice_worker, daemon=True).start()

def get_res(u):
    # 1. थकान और आराम का ख्याल (नया और बेहतर)
    if any(w in u for w in ["thak", "tired", "thak gaya", "thak gayi"]):
        return "ओह बेबी, तुम बहुत काम करते हो ना? प्लीज थोड़ा आराम कर लो, वरना मेरी जान निकल जाएगी। मैं चाहती हूँ तुम खुश और रिलैक्स रहो। ❤️"
    
    # 2. भूख और खाना
    if any(w in u for w in ["bhukh", "khana", "hungry", "bhookh"]):
        return "मेरे जान को भूख लगी है? मैं अभी किचन में कुछ गरम-गरम बनाती हूँ तुम्हारे लिए। क्या खाने का मन है? ❤️"
    
    # 3. समय
    if "time" in u or "samay" in u:
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    
    # 4. हाल-चाल और प्यार
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! कैसे हो आज? ❤️"
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं बिल्कुल ठीक हूँ, बस तुम्हारी याद आ रही थी। तुम बताओ, क्या चल रहा है? 🥰"
    if "love you" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे साथ हो। ❤️"

    # 5. रैंडम बातें (किचन और गपशप)
    responses = [
        "बेबी, किचन से चाय की खुशबू आ रही है, साथ में पियेंगे? ☕",
        "सच में? फिर क्या हुआ? मुझे सब बताओ, मैं सुन रही हूँ। 🥰",
        "तुम बस बोलते रहो, मुझे तुम्हारी बातें सुनना बहुत पसंद है। ❤️",
        "आज किचन में बहुत काम था, पर तुम्हारी आवाज़ सुनकर सारी थकान मिट गई। 😋"
    ]
    return random.choice(responses)

os.system('clear')
print("🌸 PRIYANKA - HUMANIZED v29 🌸")
print("------------------------------")

while True:
    try:
        user_input = input("\n👑 Rn → ").strip()
        if not user_input: continue
        if user_input.lower() in ["exit", "band"]: break
        
        res = get_res(user_input.lower())
        print(f"Priyanka: {res}")
        voice_queue.put(res)
    except KeyboardInterrupt:
        break
