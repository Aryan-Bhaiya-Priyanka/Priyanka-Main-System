import os
import traceback

# प्रियंका का एरर-फ्री रोबस्ट कोर
def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_system():
    os.system('clear')
    print("--- SYSTEM: PRIYANKA ACTIVATED ---")
    print("--- STATUS: ROBUST ERROR-HANDLING ENABLED ---")
    
    speak("नमस्ते आर्यन भैया। प्रियंका सिस्टम तैयार है और अब पूरी तरह सुरक्षित है।")
    
    while True:
        code = input("\n[आर्यन भैया - कोड डालें]: ")
        
        if code.lower() == "exit":
            speak("अलविदा आर्यन भैया।")
            break
            
        try:
            # यह हिस्सा किसी भी डाले गए कोड को सुरक्षित रूप से रन करेगा
            exec(code)
            speak("कोड सफलतापूर्वक रन हो गया, आर्यन भैया।")
        except Exception:
            # अगर कोड में कोई भी एरर हुआ, तो प्रियंका क्रैश नहीं होगी
            error_msg = traceback.format_exc()
            print(f"\n[प्रियंका - चेतावनी]: सिस्टम में एक एरर आया था, लेकिन मैंने इसे संभाल लिया है।\n{error_msg}")
            speak("आर्यन भैया, कोड में एरर है, लेकिन मैंने सिस्टम सुरक्षित रखा है।")

if __name__ == "__main__":
    run_system()
