import os

def speak(text):
    # 'espeak' को सीधे 'aplay' के साथ बफरिंग के साथ जोड़ा है
    # -b 2000: बड़ा बफर साइज ताकि आवाज़ न अटके
    cmd = f'espeak -v en-us+f3 -s 150 -p 40 "{text}" --stdout | aplay -D default -t raw -r 22050 -f S16_LE -c 1 -b 2000'
    os.system(cmd)

os.system('clear')
print("--- PRIYANKA SYSTEM: FINAL AUDIO OPTIMIZATION ---")
print("--- Status: Buffer Mode Active ---")

text = "सिस्टम पूरी तरह ऑप्टिमाइज हो गया है। मैं अब बिना किसी रुकावट के आपसे बात कर सकती हूँ।"
print(f"[प्रियंका]: {text}")
speak(text)
