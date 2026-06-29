#!/data/data/com.termux/files/usr/bin/bash

# यह स्क्रिप्ट तुम्हारी फोटो को हैकर लुक देगी
echo "Initializing Hacker Protocol..."
pkg install imagemagick -y
echo "Processing images..."

# यहाँ फाइल का नाम डालकर फिल्टर लगाओ (जैसे Matrix Green overlay)
convert 1000005775.jpg -fill green -tint 50 hacker_final.jpg

echo "Process Complete! Your image is ready."
