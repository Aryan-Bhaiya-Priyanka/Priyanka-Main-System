import os, datetime, random, threading, time, queue

voice_queue = queue.Queue()
# यह फ्लैग चेक करेगा कि क्या तुम अभी बात कर रहे हो
is_user_chatting = False

def voice_worker():
    while True:
        text = voice_queue.get()
        if text is None: break
        clean = text.replace('"', '').replace("'", "").replace('\n', ' ')
        os.system(f'termux-tts-speak -e com.google.android.tts -l hi-IN "{clean}" > /dev/null 2>&1')
        voice_queue.task_done()

threading.Thread(target=voice_worker, daemon=True).start()

def speak(text):
    voice_queue.put(text)

def background_logic():
    global is_user_chatting
    while True:
        time.sleep(600) # 10 मिनट का वेट
        # अगर तुम बात नहीं कर रहे, तभी वो खुद से मैसेज भेजेगी
        if not is_user_chatting:
            msgs = ["बेबी, क्या कर रहे हो?", "याद आ रही है तुम्हारी ❤️", "चाय पी ली?"]
            speak(random.choice(msgs))
        is_user_chatting = False # रिसेट

threading.Thread(target=background_logic, daemon=True).start()

while True:
    os.system("clear")
    print("🌸 PRIYANKA AI - v20.0 (Interrupt Mode) 🌸")
    user_input = input("\n👑 Rn → ").strip()
    
    if not user_input: continue
    is_user_chatting = True # अब बैकग्राउंड मैसेज नहीं आएगा
    
    u = user_input.lower()
    if any(w in u for w in ["bhukh", "khana", "biryani"]):
        res = "ओह बेबी! भूख लगी है? मैं अभी तुम्हारे लिए गरम बिरयानी ऑर्डर करती हूँ या बनाती हूँ ❤️"
    else:
        res = "हम्म, मैं सुन रही हूँ Rn..."
        
    print(f"Priyanka: {res}")
    speak(res)
