import requests , threading , random , time
from colorama import Fore , Style

"""
Developed by CRYONICX
All responsibility for the project is on you.
DISCORD = CRYONICX#9999 ID = 788124670556766209
"""
class Guild_joiner:
    def __init__(self, token , invitelink):
        liste = [""]
        self.invite_link = invitelink
        self.token = token[:-2]
        for x in liste:
            self.headers = {'Authorization': self.token}

    def guild_joiner(self):
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

            r = requests.post(f"https://discord.com/api/v9/invites/{self.invite_link}",headers=self.headers , json={'content-type:': "application/json"} , proxies=proxies)
            print(f"{Fore.GREEN} [✔] Spamming.{Style.RESET_ALL}" if r  else f"{Fore.RED}[X] Failed. {Style.RESET_ALL}")
            

        else:
            r = requests.post(f"https://discord.com/api/v9/invites/{self.invite_link}",headers=self.headers , json={'content-type:': "application/json"})
            print(f"{Fore.GREEN} [✔] Spamming.{Style.RESET_ALL}" if r  else f"{Fore.RED}[X] Failed. {Style.RESET_ALL}")
            
        return r

def worker(token , invitelink):
    lines = []
    with open('./config/tokens.txt') as f:
        lines = f.readlines()

    e = Guild_joiner(token , invitelink)
    e.guild_joiner()

def main():
    input_invite_id = input(
        f"{Fore.BLUE}{Style.BRIGHT}[?] Enter the guild invite code > {Style.RESET_ALL}")

    if input_invite_id.startswith("discord.gg/"):

        sum = input_invite_id.split("/")

        invite_code = sum[3]

    else:
        invite_code = input_invite_id

    #print(f"{invite_code}")

    lines = []
    with open('./config/tokens.txt') as f:
        lines = f.readlines()

    threads = []

    for i in lines:
        t = threading.Thread(target=worker, args=(i , invite_code,))
        threads.append(t)
        t.start()


if __name__ == '__main__':
    main()