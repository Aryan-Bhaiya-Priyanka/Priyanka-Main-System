# 1. GitHub फोल्डर में जाकर प्रियंका वाला फोल्डर बना रहे हैं
cd ~/GitHub_Projects/BlackKing
mkdir -p Priyanka

# 2. प्रियंका से जुड़ी फाइलें सिर्फ प्रियंका फोल्डर में डाल रहे हैं
# यह कमांड ढूँढेगी कि प्रियंका की कौन सी फाइल्स हैं और उन्हें सुरक्षित मूव करेगी
find ~ -maxdepth 1 -name "*priyanka*" -type f -exec mv {} ~/GitHub_Projects/BlackKing/Priyanka/ \;

# 3. गिटहब इंडेक्स अपडेट कर रहे हैं
git add Priyanka/
git commit -m "Organized Priyanka files only"

echo "आर्यन भैया, प्रियंका की सारी फाइलें अब सुरक्षित 'Priyanka' फोल्डर में हैं।"
