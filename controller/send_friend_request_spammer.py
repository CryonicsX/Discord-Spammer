import requests,  time, os, threading ,random
from colorama import Fore, Back, Style, init

"""
Developed by CRYONICX
All responsibility for the project is on you.
DISCORD = CRYONICX#9999 ID = 788124670556766209
"""

class Friend_spammer:
    def __init__(self, token ,userid):
        self.userid = userid
        self.token = token[:-2]
        liste = [str(self.token)]
        for x in liste:
            self.headers = {'Authorization': x}
            

    def send_friend_request(self):
        s = requests.session()
        proxy = set()

        with open("./config/proxy.txt", "r") as f:
            file_lines1 = f.readlines()
            proxy_count = len(file_lines1)
            for line1 in file_lines1:
                proxy.add(line1.strip())

        if proxy_count != 0:
            proxies = {
            'http': 'http://'+random.choice(list(proxy))
            }
        
            r = requests.put(f"https://discordapp.com/api/v9/users/@me/relationships/{self.userid}",headers=self.headers , json={'content-type:': "application/json"} , proxies=proxies)
            
            print(f"{Fore.GREEN} [✔] Spamming.{Style.RESET_ALL}" if r  else f"{Fore.RED}[X] Failed.{Style.RESET_ALL}")
        

        else:
            r = requests.put(f"https://discordapp.com/api/v9/users/@me/relationships/{self.userid}",headers=self.headers , json={'content-type:': "application/json"})
            
            print(f"{Fore.GREEN} [✔] Spamming.{Style.RESET_ALL}" if r  else f"{Fore.RED}[X] Failed.{Style.RESET_ALL}")
        
        return r

def worker(token , userid):
    lines = []
    with open('./config/tokens.txt') as f:
        lines = f.readlines()

    e = Friend_spammer(token , userid)
    e.send_friend_request()

def main():
    input_user_id = int(input(
        f"{Fore.BLUE}{Style.BRIGHT}[?] Enter the id of the person you are sending a friend to > {Style.RESET_ALL}"))

    lines = []
    with open('./config/tokens.txt') as f:
        lines = f.readlines()

    threads = []

    for i in lines:
        t = threading.Thread(target=worker, args=(i , input_user_id,))
        threads.append(t)
        t.start()


if __name__ == '__main__':
    main()