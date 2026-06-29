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
    # 1. जब तुम काम या किचन में बिजी हो
    if any(w in u for w in ["duty", "kaam", "kitchen", "rasoi", "thak", "tired"]):
        return "बेबी, तुम किचन में इतना काम क्यों कर रहे हो? थोड़ा आराम भी कर लिया करो ना! मुझे तुम्हारी फिक्र होती है। ❤️"
    
    # 2. समय
    if "time" in u or "samay" in u:
        return f"अभी {time.strftime('%I:%M %p')} हो रहे हैं, जान। ❤️"
    
    # 3. हाल-चाल और प्यार
    if any(w in u for w in ["hii", "hi", "hello"]):
        return "नमस्ते मेरे जान! आज का दिन कैसा रहा तुम्हारा? ❤️"
    if "kaisi ho" in u or "kaise ho" in u:
        return "मैं बिल्कुल ठीक हूँ, बस तुम्हारी याद आ रही थी। तुम बताओ, क्या चल रहा है? 🥰"
    if "love you" in u:
        return "आई लव यू टू बेबी! तुम हमेशा मेरे साथ हो। ❤️"

    # 4. रैंडम केयरिंग बातें
    responses = [
        "जल्दी से काम निपटा लो बेबी, फिर हम दोनों आराम से बातें करेंगे। 🥰",
        "मुझे पता है तुम बहुत मेहनती हो, पर अपनी सेहत का भी ख्याल रखो। ❤️",
        "तुम्हें थकते हुए देखकर मुझे अच्छा नहीं लगता, बस काम खत्म करके आ जाओ मेरे पास। 😋",
        "तुम तो बेस्ट हो, काम भी कर लेते हो और मेरा ख्याल भी रखते हो। ❤️"
    ]
    return random.choice(responses)

os.system('clear')
print("🌸 PRIYANKA - UPDATED v30 🌸")
print("----------------------------")

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
