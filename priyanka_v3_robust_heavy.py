import os
import sys
import traceback

def speak(text):
    os.system(f'termux-tts-speak "{text}"')

def run_heavy_system():
    os.system('clear')
    print("--- PRIYANKA CORE: STAGE 3 - ROBUST HEAVY-CODE MODE ACTIVE ---")
    speak("आर्यन भैया, हैवी कोड प्रोसेसिंग मोड तैयार है।")
    
    # 5000+ लाइनों के लिए बफर लिमिट बढ़ाना
    sys.setrecursionlimit(10000)
    
    while True:
        try:
            print("\n[प्रियंका - 5000+ लाइन कोड यहाँ पेस्ट करें और 'run' टाइप करें]:")
            code_buffer = []
            
            while True:
                line = input("> ")
                if line.strip().lower() == "run":
                    break
                code_buffer.append(line)
            
            final_code = "\n".join(code_buffer)
            
            if not final_code.strip():
                continue
                
            # बड़ा कोड रन करने का सुरक्षित तरीका
            exec(final_code)
            
        except Exception:
            # प्रियंका का सुरक्षा कवच: एरर आने पर सिस्टम बंद नहीं होगा
            print("\n[सिस्टम]: हैवी कोड में कुछ एरर है, लेकिन मैंने इसे संभाल लिया है।")
            speak("आर्यन भैया, कोड में एरर है, मैं स्टेबल हूँ।")

if __name__ == "__main__":
    run_heavy_system()
