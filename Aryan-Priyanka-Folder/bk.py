#!/usr/bin/env python3
import os,sys,time,json,hashlib,random,string,subprocess,datetime
D=os.path.expanduser("~/black_king")
for x in[D+"/data",D+"/reports",D+"/logs",D+"/vault"]:os.makedirs(x,exist_ok=True)
PF=D+"/data/pin.json";LF=D+"/logs/activity.log";TF=D+"/data/targets.json";NF=D+"/data/notes.json"
R="\033[1;31m";G="\033[1;32m";Y="\033[1;33m";C="\033[1;36m";W="\033[1;37m";GR="\033[1;90m";RS="\033[0m"
def speak(t):subprocess.Popen(["termux-tts-speak","-e","com.google.android.tts","-l","hi","-r","0.9",t],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
def log(a):
    with open(LF,"a")as f:f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {a}\n")
def pause():input(f"\n{GR}Enter dabao...{RS}")
def clr():os.system("clear")
def banner():
    clr()
    print(f"{R}{'='*54}{RS}")
    print(f"{R}  ██████╗ ██╗      █████╗  ██████╗██╗  ██╗{RS}")
    print(f"{R}  ██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝{RS}")
    print(f"{R}  ██████╔╝██║     ███████║██║     █████╔╝ {RS}")
    print(f"{R}  ██╔══██╗██║     ██╔══██║██║     ██╔═██╗ {RS}")
    print(f"{R}  ██████╔╝███████╗██║  ██║╚██████╗██║  ██╗{RS}")
    print(f"{R}  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝{RS}")
    print(f"{R}  ██╗  ██╗██╗███╗   ██╗ ██████╗{RS}")
    print(f"{R}  ██║ ██╔╝██║████╗  ██║██╔════╝{RS}")
    print(f"{R}  █████╔╝ ██║██╔██╗ ██║██║  ███╗{RS}")
    print(f"{R}  ██╔═██╗ ██║██║╚██╗██║██║   ██║{RS}")
    print(f"{R}  ██║  ██╗██║██║ ╚████║╚██████╔╝{RS}")
    print(f"{R}  ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝{RS}")
    print(f"{R}{'='*54}{RS}")
    print(f"{Y}  अर्यन भैया का सिस्टम अभेद्य है | BLACK KING तैनात{RS}")
    t=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"{GR}  {t}  |  CYBER MODE ACTIVE{RS}")
    print(f"{R}{'='*54}{RS}\n")
def pin_check():
    if not os.path.exists(PF):
        speak("पहली बार पिन सेट करो")
        p=input(f"{Y}Naya 4-digit PIN: {RS}").strip()
        c=input(f"{Y}Dobara: {RS}").strip()
        if p==c and len(p)==4 and p.isdigit():
            json.dump({"pin":hashlib.sha256(p.encode()).hexdigest()},open(PF,"w"))
            speak("पिन सेट हो गया");print(f"{G}PIN set!{RS}")
        else:
            json.dump({"pin":hashlib.sha256("1432".encode()).hexdigest()},open(PF,"w"))
            print(f"{Y}Default PIN 1432 set{RS}")
        return
    d=json.load(open(PF))
    for i in range(3):
        try:p=input(f"{R}[BLACK KING] PIN: {RS}").strip()
        except:sys.exit()
        if hashlib.sha256(p.encode()).hexdigest()==d["pin"]:
            speak("सिस्टम अनलॉक। अर्यन भैया तैयार हैं।");return
        print(f"{R}Galat! {2-i} mauke bache{RS}")
    speak("एक्सेस अस्वीकार");sys.exit()
def menu():
    banner()
    opts=[("1","Recon & Network Scan"),("2","OSINT & Social Recon"),("3","Defense & System Check"),("4","System Health"),("5","Targets Manager"),("6","Logs & Reports"),("7","Password Generator"),("8","Hash Calculator"),("9","Ethical Notes (Hindi)"),("10","Backup"),("11","Bulletin Board"),("12","Website Checker"),("13","WhatsApp Link"),("14","Update"),("15","Change PIN"),("0","Exit")]
    for n,l in opts:
        c=R if n=="0" else G
        print(f"  {c}[{n}]{RS}  {l}")
    print(f"\n{R}{'='*54}{RS}")
def recon():
    banner();print(f"{C}=== RECON ==={RS}\n")
    print(f"{G}[1]{RS} IP & Network Info")
    print(f"{G}[2]{RS} Connected Devices")
    print(f"{G}[3]{RS} Open Ports")
    print(f"{G}[4]{RS} nmap Scan")
    print(f"{G}[0]{RS} Wapas\n")
    speak("रीकॉन मोड")
    ch=input(f"{R}BK> {RS}").strip()
    if ch=="1":
        print(f"\n{Y}--- Network Info ---{RS}");os.system("ip addr show 2>/dev/null")
        os.system("echo 'Public IP:' && curl -s --max-time 5 ifconfig.me && echo");log("IP check")
    elif ch=="2":
        print(f"\n{Y}--- Devices ---{RS}");os.system("arp -a 2>/dev/null || ip neigh 2>/dev/null");log("ARP scan")
    elif ch=="3":
        print(f"\n{Y}--- Open Ports ---{RS}");os.system("ss -tuln 2>/dev/null");log("Port scan")
    elif ch=="4":
        t=input(f"{Y}Target IP/host: {RS}").strip()
        if t:
            ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            out=D+"/reports/scan_"+ts+".txt"
            speak("स्कैन शुरू");os.system(f"nmap -sV -T4 {t} 2>/dev/null | tee {out}")
            print(f"{G}Saved: {out}{RS}");log("nmap: "+t)
    pause()
def osint():
    banner();print(f"{C}=== OSINT ==={RS}\n")
    speak("ओसिंट मोड")
    t=input(f"{Y}Naam ya username: {RS}").strip()
    if not t:pause();return
    print(f"\n{Y}--- Results: {t} ---{RS}")
    pl=[("GitHub","https://github.com/"+t),("Instagram","https://instagram.com/"+t),("Twitter","https://twitter.com/"+t),("LinkedIn","https://linkedin.com/in/"+t),("Facebook","https://facebook.com/"+t),("YouTube","https://youtube.com/@"+t),("Telegram","https://t.me/"+t),("Reddit","https://reddit.com/u/"+t),("TikTok","https://tiktok.com/@"+t)]
    for p,u in pl:print(f"  {G}{p:<12}{RS} {u}")
    q=t.replace(" ","+")
    print(f"\n{C}--- Search Links ---{RS}")
    print(f"  {G}Google:   {RS}https://google.com/search?q={q}")
    print(f"  {G}Facebook: {RS}https://facebook.com/search/top?q={q}")
    log("OSINT: "+t)
    with open(D+"/logs/osint.log","a")as f:
        f.write(f"\n[{datetime.datetime.now()}] {t}\n")
        for p,u in pl:f.write(f"  {p}: {u}\n")
    print(f"\n{G}Log save ho gaya!{RS}");pause()
def defense():
    banner();print(f"{C}=== DEFENSE CHECK ==={RS}\n")
    speak("डिफेंस चेक")
    print(f"{Y}--- Processes ---{RS}");os.system("ps aux 2>/dev/null | head -10")
    print(f"\n{Y}--- Ports ---{RS}");os.system("ss -tuln 2>/dev/null")
    print(f"\n{Y}--- Storage ---{RS}");os.system("df -h 2>/dev/null")
    print(f"\n{Y}--- Memory ---{RS}");os.system("free -h 2>/dev/null")
    log("Defense check");pause()
def health():
    banner();print(f"{C}=== SYSTEM HEALTH ==={RS}\n")
    speak("सिस्टम हेल्थ")
    print(f"{Y}--- Battery ---{RS}");os.system("termux-battery-status 2>/dev/null")
    print(f"\n{Y}--- CPU ---{RS}");os.system("cat /proc/cpuinfo 2>/dev/null | grep 'model name' | head -2")
    print(f"\n{Y}--- Memory ---{RS}");os.system("free -h 2>/dev/null")
    print(f"\n{Y}--- Storage ---{RS}");os.system("df -h ~ 2>/dev/null")
    print(f"\n{Y}--- Uptime ---{RS}");os.system("uptime 2>/dev/null")
    print(f"\n{Y}--- Device ---{RS}");os.system("getprop ro.product.model 2>/dev/null && getprop ro.build.version.release 2>/dev/null")
    log("Health check");pause()
def targets():
    banner();print(f"{C}=== TARGETS ==={RS}\n")
    speak("टारगेट मैनेजर")
    tl=json.load(open(TF))if os.path.exists(TF)else[]
    print(f"{G}[1]{RS} Add\n{G}[2]{RS} View\n{G}[3]{RS} Delete\n{G}[0]{RS} Wapas\n")
    ch=input(f"{R}BK> {RS}").strip()
    if ch=="1":
        n=input(f"{Y}Target: {RS}").strip();nt=input(f"{Y}Note: {RS}").strip()
        if n:tl.append({"target":n,"note":nt,"added":str(datetime.datetime.now())[:10]});json.dump(tl,open(TF,"w"),indent=2);print(f"{G}Added!{RS}");log("Target: "+n)
    elif ch=="2":
        if tl:
            for i,t in enumerate(tl):print(f"  {G}{i+1}.{RS} {t['target']} | {t.get('note','')} | {t.get('added','')}")
        else:print(f"{R}Koi target nahi{RS}")
    elif ch=="3":
        if tl:
            for i,t in enumerate(tl):print(f"  {G}{i+1}.{RS} {t['target']}")
            try:
                idx=int(input(f"{Y}Number: {RS}").strip())-1
                if 0<=idx<len(tl):r=tl.pop(idx);json.dump(tl,open(TF,"w"),indent=2);print(f"{G}Deleted: {r['target']}{RS}")
            except:print(f"{R}Galat{RS}")
    pause()
def logs():
    banner();print(f"{C}=== LOGS ==={RS}\n")
    print(f"{Y}--- Activity (Last 20) ---{RS}")
    if os.path.exists(LF):os.system("tail -20 "+LF)
    print(f"\n{Y}--- Reports ---{RS}");os.system("ls -la "+D+"/reports 2>/dev/null")
    print(f"\n{Y}--- OSINT Log ---{RS}")
    ol=D+"/logs/osint.log"
    if os.path.exists(ol):os.system("tail -10 "+ol)
    pause()
def pwdgen():
    banner();print(f"{C}=== PASSWORD GENERATOR ==={RS}\n")
    speak("पासवर्ड जनरेटर")
    try:ln=int(input(f"{Y}Length (8-64): {RS}").strip());ln=max(8,min(64,ln))
    except:ln=16
    ac=string.ascii_letters+string.digits+"!@#$%^&*()_+-="
    pwds=[]
    for _ in range(5):
        p=list(random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice("!@#$%^&*")+''.join(random.choices(ac,k=ln-4)))
        random.shuffle(p);pwds.append(''.join(p))
    print(f"\n{Y}--- Passwords ({ln} chars) ---{RS}")
    for i,p in enumerate(pwds):print(f"  {G}{i+1}.{RS} {W}{p}{RS}")
    if input(f"\n{Y}Save? (y/n): {RS}").strip().lower()=="y":
        ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        open(D+"/vault/pwd_"+ts+".txt","w").write("\n".join(pwds))
        print(f"{G}Saved!{RS}");log("Passwords generated")
    pause()
def hashcalc():
    banner();print(f"{C}=== HASH CALCULATOR ==={RS}\n")
    speak("हैश कैलकुलेटर")
    print(f"{G}[1]{RS} Text\n{G}[2]{RS} File\n{G}[0]{RS} Wapas\n")
    ch=input(f"{R}BK> {RS}").strip()
    if ch=="1":
        t=input(f"{Y}Text: {RS}").strip()
        if t:
            tb=t.encode()
            print(f"\n{G}MD5:    {RS}{hashlib.md5(tb).hexdigest()}")
            print(f"{G}SHA1:   {RS}{hashlib.sha1(tb).hexdigest()}")
            print(f"{G}SHA256: {RS}{hashlib.sha256(tb).hexdigest()}")
            print(f"{G}SHA512: {RS}{hashlib.sha512(tb).hexdigest()}")
    elif ch=="2":
        fp=os.path.expanduser(input(f"{Y}Path: {RS}").strip())
        if os.path.exists(fp):
            d=open(fp,"rb").read()
            print(f"\n{G}MD5:    {RS}{hashlib.md5(d).hexdigest()}")
            print(f"{G}SHA256: {RS}{hashlib.sha256(d).hexdigest()}")
        else:print(f"{R}File nahi mili!{RS}")
    pause()
def notes_board():
    banner();print(f"{C}=== BULLETIN BOARD ==={RS}\n")
    speak("बुलेटिन बोर्ड")
    nl=json.load(open(NF))if os.path.exists(NF)else[]
    print(f"{G}[1]{RS} Naya note\n{G}[2]{RS} Dekho\n{G}[3]{RS} Delete\n{G}[0]{RS} Wapas\n")
    ch=input(f"{R}BK> {RS}").strip()
    if ch=="1":
        ti=input(f"{Y}Title: {RS}").strip();co=input(f"{Y}Note: {RS}").strip()
        if ti:nl.append({"title":ti,"content":co,"time":str(datetime.datetime.now())[:16]});json.dump(nl,open(NF,"w"),indent=2);print(f"{G}Saved!{RS}")
    elif ch=="2":
        if nl:
            for i,n in enumerate(nl):print(f"\n{G}[{i+1}] {n['title']}{RS} {GR}({n['time']}){RS}\n    {W}{n['content']}{RS}")
        else:print(f"{R}Koi note nahi{RS}")
    elif ch=="3":
        if nl:
            for i,n in enumerate(nl):print(f"  {G}{i+1}.{RS} {n['title']}")
            try:
                idx=int(input(f"{Y}Number: {RS}").strip())-1
                if 0<=idx<len(nl):r=nl.pop(idx);json.dump(nl,open(NF,"w"),indent=2);print(f"{G}Deleted: {r['title']}{RS}")
            except:pass
    pause()
def webcheck():
    banner();print(f"{C}=== WEBSITE CHECKER ==={RS}\n")
    speak("वेबसाइट चेकर")
    u=input(f"{Y}URL (jaise google.com): {RS}").strip()
    if not u:pause();return
    if not u.startswith("http"):u="https://"+u
    print(f"\n{Y}Checking {u}...{RS}")
    os.system(f"curl -s -o /dev/null -w 'Status: %{{http_code}}\\nTime: %{{time_total}}s\\n' --max-time 10 '{u}' 2>/dev/null")
    log("Website: "+u);pause()
def wagen():
    banner();print(f"{C}=== WHATSAPP LINK ==={RS}\n")
    speak("व्हाट्सएप लिंक")
    print(f"{GR}Example: 919876543210{RS}\n")
    n=input(f"{Y}Number (with country code): {RS}").strip().replace("+","").replace(" ","").replace("-","")
    if not n.isdigit():print(f"{R}Sirf numbers!{RS}");pause();return
    m=input(f"{Y}Message (optional): {RS}").strip()
    lnk=f"https://wa.me/{n}"+(f"?text={m.replace(' ','%20')}"if m else"")
    print(f"\n{G}Link:{RS}\n{W}{lnk}{RS}")
    if input(f"\n{Y}Kholun? (y/n): {RS}").strip().lower()=="y":os.system(f'termux-open-url "{lnk}" 2>/dev/null')
    log("WA: "+n);pause()
def ethical():
    banner();print(f"{C}=== ETHICAL NOTES (HINDI) ==={RS}\n")
    speak("एथिकल हैकिंग नोट्स")
    tp=[("Reconnaissance","Passive: Google Dorking, WHOIS, Shodan\nActive: Ping, nmap, Banner grabbing\nRule: Sirf apne ya permission wale systems pe!"),("nmap Guide","nmap IP → basic\nnmap -sV IP → versions\nnmap -A IP → aggressive\nnmap -T4 IP → fast\nnmap -sC IP → scripts"),("Linux Commands","ls -la | find | cat | head\nip a | ss -tuln | curl ifconfig.me\nps aux | kill PID | free -h | df -h"),("Hashing","MD5=128bit | SHA256=256bit | SHA512=512bit\nSame input = same hash\nReverse nahi ho sakta\nUse: passwords, file integrity"),("Hardening","1. pkg update regularly\n2. Strong passwords 12+ chars\n3. Open ports check: ss -tuln\n4. Logs monitor karo\n5. Regular backup\n6. VPN on public WiFi")]
    for i,(t,_)in enumerate(tp):print(f"  {G}[{i+1}]{RS} {t}")
    print(f"  {G}[0]{RS} Wapas\n")
    ch=input(f"{R}BK> {RS}").strip()
    try:
        idx=int(ch)-1
        if 0<=idx<len(tp):
            ti,co=tp[idx];print(f"\n{Y}{'='*40}{RS}\n{C}{ti}{RS}\n{Y}{'='*40}{RS}\n{W}{co}{RS}")
            speak(ti);log("Notes: "+ti)
    except:pass
    pause()
def backup():
    banner();print(f"{C}=== BACKUP ==={RS}\n")
    speak("बैकअप हो रहा है")
    ts=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    h=os.path.expanduser("~")
    bp=h+"/bk_backup_"+ts+".tar.gz"
    r=os.system(f"tar -czf {bp} -C {h} black_king/data black_king/reports black_king/logs black_king/vault 2>/dev/null")
    if r==0:print(f"{G}Backup: {bp}{RS}");speak("बैकअप पूरा");log("Backup: "+ts)
    else:print(f"{R}Problem!{RS}")
    pause()
def update():
    banner();print(f"{C}=== UPDATE ==={RS}\n")
    speak("अपडेट हो रहा है")
    os.system("pkg update -y && pkg upgrade -y")
    print(f"\n{G}Done!{RS}");speak("अपडेट पूरा");log("Update");pause()
def chpin():
    banner();print(f"{C}=== CHANGE PIN ==={RS}\n")
    if os.path.exists(PF):
        d=json.load(open(PF))
        o=input(f"{Y}Purana PIN: {RS}").strip()
        if hashlib.sha256(o.encode()).hexdigest()!=d["pin"]:print(f"{R}Galat!{RS}");pause();return
    np=input(f"{Y}Naya PIN (4 digits): {RS}").strip()
    nc=input(f"{Y}Dobara: {RS}").strip()
    if np==nc and len(np)==4 and np.isdigit():
        json.dump({"pin":hashlib.sha256(np.encode()).hexdigest()},open(PF,"w"))
        print(f"{G}PIN badal gaya!{RS}");speak("पिन बदल गया");log("PIN changed")
    else:print(f"{R}Galat! 4 digits chahiye{RS}")
    pause()
if __name__=="__main__":
    banner()
    speak("ब्लैक किंग शुरू हो रहा है। अर्यन भैया का सिस्टम अभेद्य है।")
    pin_check();log("BK launched")
    mp={"1":recon,"2":osint,"3":defense,"4":health,"5":targets,"6":logs,"7":pwdgen,"8":hashcalc,"9":ethical,"10":backup,"11":notes_board,"12":webcheck,"13":wagen,"14":update,"15":chpin}
    while True:
        menu()
        try:ch=input(f"\n{R}[BLACK KING]> {RS}").strip()
        except(KeyboardInterrupt,EOFError):print(f"\n{Y}Exit ke liye 0{RS}");continue
        if ch=="0":
            speak("ब्लैक किंग बंद हो रहा है। सिस्टम सुरक्षित रहेगा।")
            banner();print(f"{R}  BLACK KING OFFLINE{RS}\n");log("BK offline");sys.exit()
        elif ch in mp:mp[ch]()
        else:print(f"{R}0-15 mein se chuno{RS}");time.sleep(1)
