#İmports
from random import choice
from colorama import Fore, Style
#Files
import controller.guild_joiner as cryonicx1
import controller.message_spammer as cryonicx2
import controller.send_friend_request_spammer as cryonicx3


with open("./config/proxy.txt", "r") as f:
  file_lines1 = f.readlines()
  proxy_count = len(file_lines1)

with open("./config/tokens.txt", "r") as f:
  file_lines2 = f.readlines()
  token_count = len(file_lines2)



intro = f'''{Fore.BLUE} {Style.BRIGHT}
    ____  _                          __   _____                                             Developed by CRYONICX
   / __ \(_)_____________  _________/ /  / ___/____  ____ _____ ___  ____ ___  ___  _____   
  / / / / / ___/ ___/ __ \/ ___/ __  /   \__ \/ __ \/ __ `/ __ `__ \/ __ `__ \/ _ \/ ___/
 / /_/ / (__  ) /__/ /_/ / /  / /_/ /   ___/ / /_/ / /_/ / / / / / / / / / / /  __/ /    
/_____/_/____/\___/\____/_/   \__,_/   /____/ .___/\__,_/_/ /_/ /_/_/ /_/ /_/\___/_/   
                                           /_/                                           

All responsibility in the project is on you, I'm just a developer.

Accounts may be at risk of being closed!

If you find a bug in the project, you can contact me on discord. Discord = CRYONICX#9999

-------------------------------------------------------------------------

{Fore.LIGHTWHITE_EX}Proxys : {proxy_count} 
Tokens : {token_count}{Style.RESET_ALL}{Fore.BLUE}{Style.BRIGHT}

1) Join Guild
2) Message Spammer (DM/CHANNEL)
3) Friend Spammer
4) Quit

-------------------------------------------------------------------------
{Style.RESET_ALL}'''

print(intro)

choice = input(f"{Fore.BLUE}{Style.BRIGHT}[?] >{Style.RESET_ALL}  ")


if choice == "1":
  cryonicx1.main()

if choice == "2":
  cryonicx2.main()

if choice == "3":
  cryonicx3.main()


if choice == "4":
  quit()