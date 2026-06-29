import os

# 1. इंस्टॉलेशन चेक (स्मूथ इंजन के लिए)
os.system('pkg install espeak-ng -y > /dev/null 2>&1')

def speak(text):
    # -s 170: बोलने की गति (ना ज्यादा तेज़, ना धीमी)
    # -p 60: पिच (इसे थोड़ा ऊपर रखा है ताकि आवाज़ में जोश रहे)
    # -v en-us+f3: अमेरिकन फीमेल आवाज़ जो काफी नेचुरल है
    cmd = f'espeak-ng -v en-us+f3 -s 170 -p 60 "{text}"'
    os.system(cmd)

def run():
    os.system('clear')
    print("--- PRIYANKA v31: VOICE OPTIMIZED ---")
    
    welcome = "नमस्ते, मैं प्रियंका हूँ। अब मेरी आवाज़ बिल्कुल साफ़ और ऊर्जावान है।"
    speak(welcome)
    
    while True:
        user_input = input("\n[आप]: ")
        if "exit" in user_input: break
        
        reply = "मैं सुन रही हूँ, आप आगे की बात बताइए।"
        print(f"[प्रियंका]: {reply}")
        speak(reply)

run()
