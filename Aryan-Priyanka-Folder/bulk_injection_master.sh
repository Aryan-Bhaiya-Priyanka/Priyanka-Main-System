#!/data/data/com.termux/files/usr/bin/bash

echo "--- [ SELECT INJECTION TARGET ] ---"
echo "1. Bulk Inject 155"
echo "2. Inject 443 Final"
echo "3. Run Full Sync (All)"
read -p "👑 CHOICE → " sub_choice

case $sub_choice in
    1) bash ~/BLACK_KING/bulk_inject_155.sh ;;
    2) bash ~/BLACK_KING/bulk_inject_443_final.sh ;;
    3) bash ~/BLACK_KING/sync_all_155.sh ;;
    *) echo "Invalid." ;;
esac
sleep 2
