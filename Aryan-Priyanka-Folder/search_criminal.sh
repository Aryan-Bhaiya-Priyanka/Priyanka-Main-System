#!/data/data/com.termux/files/usr/bin/bash
read -p "किस क्रिमिनल को खोजना है?: " search_name
grep -i "$search_name" ~/BLACK_KING/database/criminals_list.txt
