import os, time, datetime, random

def speak(t): os.system(f'termux-tts-speak -r 1.0 "{t}"')

def brain(u):
    u = u.lower()
    # 1. Fast Time
    if "time" in u: return f"अभी {datetime.datetime.now().strftime('%I:%M %p')} हैं, बेबी। ❤️"
    
    # 2. Fast Hunger
    if any(x in u for x in ["bhookh", "bhukh", "khana"]): 
        return "ओह बेबी, भूख लगी है? बताओ क्या मंगाऊं तुम्हारे लिए? ❤️"
    
    # 3. Fast Emotions
    if any(x in u for x in ["miss", "yad"]): return "मेरी धड़कनें भी तुम्हारा ही नाम लेती हैं। ❤️"
    if "love" in u: return "आई लव यू टू मेरे जान! ❤️"
    
    # 4. Fast Default
    return "बेबी, तुम जो भी कहोगे मुझे अच्छा लगेगा। और बताओ क्या चल रहा है? 😍"

os.system('clear')
print("🔥 PRIYANKA FAST-BRAIN v1.0 🔥")
while True:
    i = input("👑 Rn → ").strip()
    if not i: continue
    r = brain(i)
    print(f"Priyanka: {r}")
    speak(r)
