import os, datetime, random, threading, time, queue

# वॉयस के लिए क्यू (Queue) सिस्टम
voice_queue = queue.Queue()

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        # Google TTS इंजन को बैकग्राउंड में चला रहे हैं
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

# वॉयस वर्कर थ्रेड चालू
threading.Thread(target=voice_worker, daemon=True).start()

while True:
    os.system("clear")
    print("🌸 PRIYANKA AI - ACTIVE (Multi-Tasking Mode) 🌸")
    user_input = input("\nRn -> ").strip()
    
    if not user_input: continue
    if user_input.lower() in ["exit", "bye"]: break
    
    t = user_input.lower()
    if "time" in t or "samay" in t:
        res = f"Rn, abhi {datetime.datetime.now().strftime('%I:%M %p')} ho raha hai."
    elif "date" in t or "aaj" in t:
        res = f"Aaj {datetime.datetime.now().strftime('%d %B %Y')} hai Rn."
    else:
        res = random.choice(["Haan jaan, main sun rahi hun!", "Rn, tum ho toh sab theek hai.", "Aur batao na Rn!"])
    
    # टेक्स्ट और वॉइस अब एक साथ चलेंगे
    print(f"Priyanka: {res}")
    voice_queue.put(res)
