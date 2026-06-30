# 1. मेमोरी बचाने के लिए फालतू फाइलें हटा रहे हैं
cd ~
rm -rf tur install_cap.sh fix_setup.sh

# 2. गिटहब के लिए एक नया 'Lightweight' फोल्डर
mkdir -p ~/GitHub_Projects/BlackKing
cd ~/GitHub_Projects/BlackKing

# 3. टूल्स सीधे गिटहब से चलाएंगे, इंस्टॉल नहीं करेंगे
git init
echo "Priyanka and Black King project managed via GitHub" > README.md
git add .
git commit -m "Initial setup for memory efficiency"

echo "Setup complete! अब सब कुछ ~/GitHub_Projects/BlackKing में रहेगा।"
