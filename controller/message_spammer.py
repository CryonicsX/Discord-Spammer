import requests , threading , random , time
from colorama import Fore , Style

"""
Developed by CRYONICX
All responsibility for the project is on you.
DISCORD = CRYONICX#9999 ID = 788124670556766209
"""

class Message_spammer:
    def __init__(self, token , channel_id ,message):
        liste = [""]
        self.message = message
        self.channel = channel_id
        self.token = token[:-2]
        for x in liste:
            self.headers = {'Authorization': self.token}

    def send_message(self):
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

            r = requests.post(f"https://discord.com/api/v9/channels/{self.channel}",headers=self.headers , json={'content-type:': "application/json" , 'content' : self.message} , proxies=proxies)
            print(f"{Fore.GREEN} [✔] Spamming.{Style.RESET_ALL}" if r  else f"{Fore.RED}[X] Failed. {Style.RESET_ALL}")
        

        else:
            r = requests.post(f"https://discord.com/api/v9/channels/{self.channel}",headers=self.headers , json={'content-type:': "application/json" , 'content' : self.message})

            print(f"{Fore.GREEN} [✔] Spamming.{Style.RESET_ALL}" if r  else f"{Fore.RED}[X] Failed.{Style.RESET_ALL}")

        return r

def worker(token , message , channel):
    lines = []
    with open('./config/tokens.txt') as f:
        lines = f.readlines()

    e = Message_spammer(token , message , channel)
    while True:
        e.send_message()

def main():

    channel_id_input = input(
        f"{Fore.BLUE}{Style.BRIGHT}[?] Enter the id of the channel you are spamming > {Style.RESET_ALL}")

    if len(channel_id_input) != 18:
        print(f"{Fore.RED}[!] Invalid id {Style.RESET_ALL}")
        time.sleep(2)
        quit()

    message_content = input(
        f"{Fore.BLACK}{Style.BRIGHT}[?] Type the message you want to spam > {Style.RESET_ALL}")


    lines = []
    with open('./config/tokens.txt') as f:
        lines = f.readlines()

    threads = []

    for i in lines:
        t = threading.Thread(target=worker, args=(i , channel_id_input ,message_content,))
        threads.append(t)
        t.start()


if __name__ == '__main__':
    main()