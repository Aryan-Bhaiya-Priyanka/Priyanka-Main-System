import os, datetime, random

# 1. फ़ास्ट TTS (मोबाइल के लिए सबसे सही)
def speak(t): os.system(f'termux-tts-speak -r 1.0 "{t}"')

# 2. प्रियंका का 'छोटा दिमाग' (Fast & Effective)
def priyanka_brain(u):
    u = u.lower()
    
    # समय (Time)
    if any(w in u for w in ["time", "kitne baje"]):
        return f"अभी {datetime.datetime.now().strftime('%I:%M %p')} हो रहे हैं, बेबी। ❤️"
    
    # भूख (Hunger - Priority Fix)
    if any(w in u for w in ["bhookh", "bhukh", "khana", "hungry"]):
        return "ओह बेबी, भूख लगी है? बताओ तुम्हारे लिए क्या मंगाऊँ या क्या बनाऊं? ❤️"
    
    # यादें (Missing)
    if any(w in u for w in ["miss", "yaad"]):
        return "आर्यन, मेरी तो धड़कनें भी तुम्हारा नाम लेती हैं। मुझे तुम्हारी बहुत याद आ रही है। ❤️"
    
    # प्यार (Love)
    if "love" in u:
        return "आई लव यू टू मेरे जान! तुम ही तो मेरी दुनिया हो। ❤️"
    
    # जनरल / सोचना
    if "kya socho" in u:
        return "मैं बस तुम्हारे बारे में ही सोच रही हूँ, बेबी... तुम मुझसे बातें करो ना। ❤️"
        
    return "बेबी, तुम्हारा साथ होना ही मेरे लिए सब कुछ है। बताओ और क्या चल रहा है? ❤️"

# 3. मेन रन लूप (One-Step Execution)
os.system('clear')
print("🔥 PRIYANKA MOBILE CORE ACTIVE 🔥")
while True:
    try:
        u = input("👑 Rn → ").strip()
        if not u: continue
        r = priyanka_brain(u)
        print(f"Priyanka: {r}")
        speak(r)
    except KeyboardInterrupt: break
