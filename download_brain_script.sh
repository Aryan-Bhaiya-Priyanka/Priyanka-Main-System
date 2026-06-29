# यह कमांड सर्वर से सीधे फाइल उठाएगी
# (यहाँ हम ओला मा/लांबा का लिंक सेट कर सकते हैं)
cd Priyanka_Brain
wget -q --show-progress "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf" -O brain_model.gguf
echo "प्रियंका का दिमाग सर्वर पर डाउनलोड हो गया है!"
