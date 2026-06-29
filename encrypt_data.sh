#!/data/data/com.termux/files/usr/bin/bash

echo "[+] ENCRYPTING VITAL DATA LAYERS..."
# डेटा को पासवर्ड के साथ लॉक करना
tar -czf - ~/BLACK_KING/data | openssl enc -aes-256-cbc -e -k "ARYAN_SECURE_123" -out ~/BLACK_KING/data.enc
rm -rf ~/BLACK_KING/data/*
echo "[+] ENCRYPTION COMPLETE: DATA IS NOW A LOCKED VAULT."
