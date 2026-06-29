#!/data/data/com.termux/files/usr/bin/bash
DIR=~/BLACK_KING/database/legends
mkdir -p $DIR

cat << 'DATA' > $DIR/hacker_archetypes.txt
[HACKER_ARCHETYPES]
1. THE_SOCIAL_ENGINEER: (e.g., Mitnick) - Targets human trust via manipulation.
2. THE_BOTMASTER: (e.g., Ancheta/Mafiaboy) - Targets infrastructure via automation and botnets.
3. THE_INDUSTRIAL_THIEF: (e.g., Gonzalez) - Targets financial data via SQL injection and business compromise.
4. THE_GHOST: (e.g., ASTRA) - Targets specialized trade secrets; stays hidden for years.
5. THE_IDEOLOGIST: (e.g., Anonymous) - Targets reputations via disruption and leaks.
DATA

echo "[+] 10 महान हैकर्स का डेटाबेस 'ब्लैक किंग' में समाहित हो गया है।"
