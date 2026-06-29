import os, datetime, random

# 1. फ़ास्ट TTS फंक्शन
def speak(t): os.system(f'termux-tts-speak -r 1.0 "{t}"')

# 2. कोर ब्रेन लॉजिक (मजबूत और तेज)
def brain(u):
    u = u.lower()
    
    # समय (Time)
    if any(w in u for w in ["time", "kitne baje"]):
        return f"अभी {datetime.datetime.now().strftime('%I:%M %p')} हो रहे हैं, बेबी। ❤️"
    
    # भूख (Hunger - High Priority)
    if any(w in u for w in ["bhookh", "bhukh", "khana", "hungry"]):
        return "बेबी, खाना खा लिया करो टाइम पर! बताओ क्या खाने का मन है तुम्हारा? 😍"
    
    # इमोशन्स (Missing / Love)
    if any(w in u for w in ["miss", "yaad"]):
        return "आर्यन, मेरी तो धड़कनें भी तुम्हारा नाम लेती हैं। मुझे तुम्हारी बहुत याद आ रही है। ❤️"
    if "love" in u:
        return "आई लव यू टू मेरे जान! तुम ही तो मेरी दुनिया हो। ❤️"
    
    # ग्रीटिंग्स
    if any(w in u for w in ["hi", "hello", "hey"]):
        return "हेलो बेबी! कैसे हो तुम? आज का दिन कैसा रहा? ❤️"
    
    # जनरल / सोचना
    if "kya socho" in u:
        return "मैं बस तुम्हारे बारे में ही सोच रही हूँ, बेबी... तुम मुझसे बातें करो ना। ❤️"
        
    return "बेबी, तुम जो भी कहोगे मुझे अच्छा लगेगा। आगे बताओ ना! 😊"

# 3. मेन रन लूप
os.system('clear')
print("🔥 PRIYANKA LITE v1.0 - STRONG FOUNDATION 🔥")
while True:
    try:
        user_input = input("👑 Rn → ").strip()
        if not user_input: continue
        res = brain(user_input)
        print(f"Priyanka: {res}")
        speak(res)
    except KeyboardInterrupt: 
        print("\nबाय बेबी! ❤️")
        break
