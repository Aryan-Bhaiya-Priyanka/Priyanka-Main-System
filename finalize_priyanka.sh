# 1. GitHub फोल्डर में वापस चलते हैं
cd ~/GitHub_Projects/BlackKing

# 2. सारी फाइलें जो प्रियंका से संबंधित हैं, उन्हें ढूंढकर अंदर डाल रहे हैं
# यह कमांड उन सभी फाइल्स को ढूँढ लेगी जो अभी बाहर बची हैं
find ~ -maxdepth 1 -name "*priyanka*" -exec mv {} ~/GitHub_Projects/BlackKing/Priyanka/ \; 2>/dev/null

# 3. अब सब कुछ गिट में ऐड करके कमिट कर रहे हैं
git add Priyanka/
git commit -m "Full backup of all Priyanka files to GitHub"

echo "आर्यन भैया, प्रियंका की एक-एक फाइल अब 'Priyanka' फोल्डर में सुरक्षित है!"
