# 1. पहले अपनी फाइल्स को एक सेफ जगह कॉपी कर लो (ताकि कुछ डिलीट न हो)
mkdir -p ~/Backup_Priyanka
cp -r ~/* ~/Backup_Priyanka/ 2>/dev/null

# 2. अब सीधे Aryan रिपॉजिटरी वाले फोल्डर में जाओ
cd ~/Aryan

# 3. यहां से पुराने कनेक्शन हटाओ और नई रिपॉजिटरी को सेट करो
git remote remove origin
git remote add origin https://github.com/Aryan-Bhaiya-Priyanka/Aryan.git

# 4. अब सारी फाइल्स यहाँ डालो और पुश करो
cp -r ~/Backup_Priyanka/* .
git add .
git commit -m "प्रियंका का सारा डेटा अब सुरक्षित है"
git push -u origin main
