#!/data/data/com.termux/files/usr/bin/bash
DIR=~/BLACK_KING/database/dns_intel
mkdir -p $DIR

cat << 'DATA' > $DIR/dns_risk_matrix.txt
[DNS_THREAT_PARAMETERS]
1. CNAME_CHAIN_LENGTH: >3 chains = HIGH_RISK (Potential Redirect Attack).
2. OUT_OF_BALLIWICK_NS: If nameservers are in different TLDs (e.g., .com vs .net), INCREASE_MONITORING.
3. GLUE_RECORD_TRUST: If server is outside the delegated zone, verify RRSIG.
4. COLD_START_VULNERABILITY: Monitor systems that frequently flush DNS cache.
DATA

echo "[+] DNS थ्रेट मैट्रिक्स 'ब्लैक किंग' में सफलतापूर्वक जुड़ गया है।"
