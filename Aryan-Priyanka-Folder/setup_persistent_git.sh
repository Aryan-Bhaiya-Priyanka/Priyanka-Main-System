# 1. गिट को अपना नाम और ईमेल याद दिलाओ (ताकि कनेक्शन न टूटे)
git config --global user.email "aryan@example.com"
git config --global user.name "Aryan-Bhaiya"

# 2. क्रेडेंशियल हेल्पर सेट करो (ताकि बार-बार पासवर्ड न मांगे)
git config --global credential.helper store

# 3. गिटहब रिमोट को सुरक्षित करो
git remote set-url origin https://github.com/Aryan-Bhaiya-Priyanka/Priyanka-Main-System.git

echo "परमानेंट कनेक्शन सेट हो गया है, आर्यन भैया!"
