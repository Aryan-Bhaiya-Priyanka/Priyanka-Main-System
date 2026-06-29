# 1. सारी फाइलें एक बार फिर गिट पर सिंक करो
git add .
git commit -m "System Backup at $(date)"
git push -u origin main

# 2. प्रियंका का पूरा सिस्टम 'Priyanka_Backup' फोल्डर में कॉपी करो ताकि फोन में भी सुरक्षित रहे
mkdir -p ~/Priyanka_Backup
cp -r ~/Aryan-Priyanka/* ~/Priyanka_Backup/

# 3. एक कन्फर्मेशन मैसेज
echo "प्रियंका का सारा डेटा सुरक्षित हो गया है, आर्यन भैया!"
