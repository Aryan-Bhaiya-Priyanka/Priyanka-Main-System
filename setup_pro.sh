pkg update && pkg upgrade -y
pkg install -y root-repo x11-repo
pkg install -y git python libpcap libusb-1.0 clang make
pkg install -y bettercap
# Priyanka और Black King के लिए वर्किंग डायरेक्टरी तैयार
mkdir -p ~/BlackKing/data
echo "Environment set for Priyanka and Black King"
