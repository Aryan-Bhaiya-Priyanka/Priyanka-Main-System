#!/bin/bash
# विनयागर मानक: प्रियंका डेटा माइग्रेशन
mkdir -p ~/Aryan
echo "[+] आर्यन फोल्डर तैयार है।"
mv ~/*priyanka* ~/Aryan/ 2>/dev/null
echo "[+] प्रियंका का सारा डेटा ~/Aryan/ में मूव कर दिया गया है।"
ls -F ~/Aryan/
echo "[!] माइग्रेशन पूर्ण।"
