import sys

# पुरानी फाइल पढ़ना
with open('priyanka.py', 'r') as f:
    lines = f.readlines()

# नया कोड लिखना जिसमें लूप नहीं है और वॉइस फंक्शन है
with open('priyanka.py', 'w') as f:
    for line in lines:
        # यहाँ हम उस लाइन को हटा रहे हैं जो लूप में फँसा रही थी
        if "तुम और बताओ आर्यन" not in line:
            f.write(line)
    
    # अब सही वॉइस फंक्शन जोड़ रहे हैं
    f.write("\nimport os\n")
    f.write("def speak(text):\n")
    f.write("    os.system('termux-tts-speak \"' + text + '\"')\n")
    f.write("print('Priyanka Voice System Active')\n")

