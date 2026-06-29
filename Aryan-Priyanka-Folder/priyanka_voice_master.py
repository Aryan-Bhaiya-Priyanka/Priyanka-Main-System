import sys
import os
import traceback

def speak(text):
    # यह टर्मक्स की वॉयस कमांड है जो हर बार आपको रिस्पॉन्स देगी
    os.system(f'termux-tts-speak "{text}"')

def run_voice_system():
    os.system('clear')
    print("--- PRIYANKA CORE: VOICE-ACTIVE STABLE v1001 ---")
    speak("आर्यन भैया, वॉयस रिस्पॉन्सिव मोड सक्रिय है। प्रियंका तैयार है।")
    
    sys.setrecursionlimit(500000)
    
    while True:
        print("\n[प्रियंका - कोड डालें (EXECUTE लिखें)]:")
        code_stream = []
        while True:
            line = input()
            if line.strip().upper() == "EXECUTE":
                break
            code_stream.append(line)
        
        final_code = "\n".join(code_stream)
        if not final_code.strip(): continue
            
        try:
            exec(final_code, {'__name__': '__main__'})
            speak("कोड सफलतापूर्वक रन हो गया है।")
        except Exception as e:
            print(f"\n[सिस्टम सुरक्षित]: एरर आया।")
            speak("आर्यन भैया, कोड में एरर है, लेकिन सिस्टम सुरक्षित है।")

if __name__ == "__main__":
    run_voice_system()
