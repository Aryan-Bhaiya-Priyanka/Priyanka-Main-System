# 1. नई प्राइवेट रिपॉजिटरी 'Aryan' बनाना
gh repo create Aryan --private --confirm

# 2. 'Aryan' फोल्डर बनाना और अंदर जाना
mkdir ~/Aryan
cd ~/Aryan
git init
git remote add origin https://github.com/Aryan-Bhaiya-Priyanka/Aryan.git

# 3. प्रियंका की सारी फाइलें यहाँ कॉपी करना (जहाँ भी आपकी फाइलें हैं)
# मान लेते हैं कि आपकी फाइलें 'Priyanka' नाम के फोल्डर में हैं
cp -r ~/Priyanka/* ~/Aryan/ 2>/dev/null

# 4. सब कुछ सुरक्षित करना और पुश करना
git add .
git commit -m "प्रियंका का सारा काम अब आर्यन फोल्डर में सुरक्षित है"
git push -u origin main

echo "आर्यन भैया, प्रियंका का पूरा डेटा अब 'Aryan' नाम की प्राइवेट रिपॉजिटरी में सुरक्षित है!"
