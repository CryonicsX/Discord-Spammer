# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->

import src as s
import threading, json, os, time, random

userids = open("./config/users.txt", "+r", encoding="utf-8").read().splitlines()
messages = open("./config/messages.txt", "+r", encoding="utf-8").read().splitlines()
tokens = open("./config/tokens.txt", "+r", encoding="utf-8").read().splitlines()
pp = open("./config/proxies.txt", "+r", encoding="utf-8").read().splitlines()
config = json.loads(open("./config/config.json", "r", encoding="utf-8").read())



class color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    BACK = '\033[1A'



def config_filler(config):
    license = str(input(f"{color.CYAN}[->]{color.RESET} Enter your program license "))
    prx = int(input(f"{color.CYAN}[->]{color.RESET} Do you want to use proxy (1: True, 0: False) "))
    api_V = str(input(f"{color.CYAN}[->]{color.RESET} Enter discord api version (6,7,8,9,10) "))
    sleep_delay = int(input(f"{color.CYAN}[->]{color.RESET} Enter sleep delay for program "))
    use_ws = int(input(f"{color.CYAN}[->]{color.RESET} Do you want use websocket (1: True, 0: False) "))
    debug_mode = int(input(f"{color.CYAN}[->]{color.RESET} Do you want open debug mode  (1: True, 0: False) "))
    proxy_protocol = str(input(f"{color.CYAN}[->]{color.RESET} Enter proxy protocool (HTTP, SOCKS5) "))
    thread_count = int(input(f"{color.CYAN}[->]{color.RESET} Enter thread count for program "))
    apiid = str(input(f"{color.CYAN}[->]{color.RESET} Enter nocaptcha uid "))
    apikey = str(input(f"{color.CYAN}[->]{color.RESET} Enter nocaptcha api key  "))
    capsolver = str(input(f"{color.CYAN}[->]{color.RESET} Enter capsolver api key  "))

    
    config["program_license"] = license
    config["use_proxy"] = True if prx == 1 else False
    config["api_version"] = api_V
    config["sleep_delay"] = sleep_delay
    config["use_websocket"] = True if use_ws == 1 else False
    config["debug_mode"] = True if debug_mode == 1 else False
    config["proxy_protocol"] = proxy_protocol
    config["thread_count"] = thread_count
    config["nocaptcha_api"]["uid"] = apiid
    config["nocaptcha_api"]["apikey"] = apikey
    config["capsolver"]["apikey"] = capsolver

    with open('./config/config.json', 'w') as f:
        json.dump(config, f)



def function_worker(proxy: dict, useragent: str, token: str, type: int, target_id: str = None, message_content: str = None, guild_code: str = None, guild_id: str = None, avatar_url: str = None, channel_id: str = None, message_id: str = None, emoji: str = None, username: str = None):
    # type_1 = dm spam
    # type_2 = guild joiner
    
    if type == 1:

        hs = s.HttpSession(proxy, useragent, token)
        hs.get_cookies()
        session = hs.session

        discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])

        discord.send_directmessage(
            target_id=target_id,
            content=message_content
        )

    elif type == 2:

        hs = s.HttpSession(proxy, useragent, token)
        hs.get_cookies()
        session = hs.session

        discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])
    
        discord.join_guild(
            guild_code
        )


    elif type == 3:
        
        hs = s.HttpSession(proxy, useragent, token)
        hs.get_cookies()
        session = hs.session

        discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])

        discord.left_guild(
            guild_id
        )


    elif type == 4:

        hs = s.HttpSession(proxy, useragent, token)
        hs.get_cookies()
        session = hs.session

        discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])

        discord.avatar_changer(
            avatar_url
        )

    elif type == 5:

        hs = s.HttpSession(proxy, useragent, token)
        hs.get_cookies()
        session = hs.session

        discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])

        discord.emoji_react(
            channel_id,
            message_id, 
            emoji
        )

    elif type == 6:

        hs = s.HttpSession(proxy, useragent, token)
        hs.get_cookies()
        session = hs.session

        discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])

        discord.friend_requester(
            username
        )



def script_worker():
    """
    check = s.check_license(config["program_license"], s.get_uuid())
    if not check[0]:
        print(f"{color.RED}[-]{color.RESET} License Error:  {check[1]}")
        return
    """
    os.system("cls" if os.name == "nt" else "clear")

    #proxies = None
    
    if config["use_proxy"]:
        print(f"{color.CYAN}[*]{color.RESET} Proxy using...")
        c_prx = s.Proxy(config).check_proxies()
        if c_prx[0] is not True:
            print(f"{color.RED}[!]{color.RESET} Proxies not working ...")
            return False
        
        proxies_ = c_prx[1]



    print(fr"""{color.CYAN} 

_________                             .___________ ____  ___
\_   ___ \_______ ___.__. ____   ____ |__\_   ___ \\   \/  /
/    \  \/\_  __ <   |  |/  _ \ /    \|  /    \  \/ \     / 
\     \____|  | \/\___  (  <_> )   |  \  \     \____/     \ 
 \______  /|__|   / ____|\____/|___|  /__|\______  /___/\  \
        \/        \/                \/           \/      \_/

    {color.RESET}
    {color.CYAN}[*]{color.RESET} Version: 1.0                       
    {color.CYAN}[*]{color.RESET} Telegram: @cryonicx
    

    {color.CYAN}[TOTAL_TOKEN]{color.RESET}: {len(tokens)}
    {color.CYAN}[TOTAL_PROXIES]{color.RESET}: {len(pp) if config['use_proxy'] else None} 
    {color.CYAN}[TOTAL_USERS]{color.RESET}: {len(userids)} 
    {color.CYAN}[HCAPTCHA_SOLVER_STATUS]{color.RESET}: ACTIVE
    {color.CYAN}[LICENSE]{color.RESET}: ACTIVE  

    {color.CYAN}[1]{color.RESET} Set the config file
    {color.CYAN}[2]{color.RESET} Start tool
    {color.CYAN}[3]{color.RESET} Exit

    Tool:
        --> {color.CYAN}[1]{color.RESET} Mass DM
        --> {color.CYAN}[2]{color.RESET} MASS JOIN
        --> {color.CYAN}[3]{color.RESET} MASS LEFT
        --> {color.CYAN}[4]{color.RESET} MASS JOİN & DM
        --> {color.CYAN}[5]{color.RESET} AVATAR CHANGER
        --> {color.CYAN}[6]{color.RESET} MEMBER SCRAPER
        --> {color.CYAN}[7]{color.RESET} Mass Emoji Reacter
        --> {color.CYAN}[7]{color.RESET} User Friend Requester
""")

    _c = int(input(f"{color.CYAN}[->]{color.RESET} "))
    
    _X = len(userids) // len(tokens)
    if _X == 0:
        _X=+1


    if _c == 1:
        print("Config setter opening ... 1.5sec")
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")
        config_filler(config)
        print(f"{color.CYAN}[+]{color.RESET} Config Filled .... 1.5sec")
        time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")
        script_worker()


    elif _c == 2:
        print(f"{color.CYAN}[+]{color.RESET} Script starting ... 1.5sec")
        #time.sleep(1.5)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"""    
--> {color.CYAN}[1]{color.RESET} Mass DM
--> {color.CYAN}[2]{color.RESET} MASS JOIN
--> {color.CYAN}[3]{color.RESET} MASS LEFT
--> {color.CYAN}[4]{color.RESET} AVATAR CHANGER
--> {color.CYAN}[5]{color.RESET} MEMBER SCRAPER
--> {color.CYAN}[6]{color.RESET} Mass Emoji Reacter
--> {color.CYAN}[7]{color.RESET} User Friend Requester
        """)
        __c = int(input(f"{color.CYAN}[->]{color.RESET} "))


        if __c == 1:
            _C = str(input(f"{color.CYAN}[->]{color.RESET} Enter Message Content "))
            os.system("cls" if os.name == "nt" else "clear")
            for token, user in zip(sorted(tokens * _X), userids):
                proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None
                if threading.active_count() < int(config["thread_count"]):
                    t = threading.Thread(target=function_worker, args=(proxies, None, token.split(":")[2], 1, user, _C))
                    time.sleep(config["sleep_delay"])
                    t.start()
        
        elif __c == 2:
            _g = str(input(f"{color.CYAN}[->]{color.RESET} Please Enter guild invite code ex:(python) "))
            os.system("cls" if os.name == "nt" else "clear")
            for token, user in zip(sorted(tokens * _X), userids):
                proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None
                if threading.active_count() < int(config["thread_count"]):
                    t = threading.Thread(target=function_worker, args=(proxies, None, token.split(":")[2], 2, None, None, _g))
                    time.sleep(config["sleep_delay"])
                    t.start()

        elif __c == 3:
            _g = str(input(f"{color.CYAN}[->]{color.RESET} Please Enter guild id "))
            os.system("cls" if os.name == "nt" else "clear")
            for token, user in zip(sorted(tokens * _X), userids):
                proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None
                if threading.active_count() < int(config["thread_count"]):
                    t = threading.Thread(target=function_worker, args=(proxies, None, token.split(":")[2], 3, None, None, None, _g))
                    time.sleep(config["sleep_delay"])
                    t.start()

        elif __c == 4:
            _g = str(input(f"{color.CYAN}[->]{color.RESET} Please Enter avatar url "))
            os.system("cls" if os.name == "nt" else "clear")
            for token, user in zip(sorted(tokens * _X), userids):
                proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None
                if threading.active_count() < int(config["thread_count"]):
                    t = threading.Thread(target=function_worker, args=(proxies, None, token.split(":")[2], 4, None, None, None, None, _g))
                    time.sleep(config["sleep_delay"])
                    t.start()


        elif __c == 5:
            proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None

            _t = str(input(f"{color.CYAN}[->]{color.RESET} Please enter scraper token "))
            _gc = str(input(f"{color.CYAN}[->]{color.RESET} Please enter guild invite code "))
            _g = str(input(f"{color.CYAN}[->]{color.RESET} Please enter guild id "))
            _c = str(input(f"{color.CYAN}[->]{color.RESET} Please enter channel id "))
            os.system("cls" if os.name == "nt" else "clear")

            hs = s.HttpSession(proxies, None, _t)
            hs.get_cookies()
            session = hs.session

            discord = s.discord_api(session, config["api_version"], use_websocket=config["use_websocket"])

            discord.scrape_members(
                _t, _g, _c, _gc
            )


        elif __c == 6:
            _c = str(input(f"{color.CYAN}[->]{color.RESET} Please enter channel id "))
            _m = str(input(f"{color.CYAN}[->]{color.RESET} Please enter message id "))
            _r = input(f"{color.CYAN}[->]{color.RESET} Please enter emoji  ")

            os.system("cls" if os.name == "nt" else "clear")
            
            for token, user in zip(sorted(tokens * _X), userids):
                proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None
                if threading.active_count() < int(config["thread_count"]):
                    t = threading.Thread(target=function_worker, args=(proxies, None, token.split(":")[2], 5, None, None, None, None, None, _c, _m, _r))
                    time.sleep(config["sleep_delay"])
                    t.start()


        elif __c == 7:
            _g = str(input(f"{color.CYAN}[->]{color.RESET} Please Enter username and discriminator eg(r00tz#0073)  "))
            os.system("cls" if os.name == "nt" else "clear")
            for token, user in zip(sorted(tokens * _X), userids):
                proxies = {"http": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}", "https": f"{config['proxy_protocol'].lower()}://{random.choice(proxies_)}"} if config["use_proxy"] else None
                if threading.active_count() < int(config["thread_count"]):
                    t = threading.Thread(target=function_worker, args=(proxies, None, token.split(":")[2], 6, None, None, None, None, None, None, None, None, _g))
                    time.sleep(config["sleep_delay"])
                    t.start()




if __name__ == "__main__":
    script_worker()
    #x = input("....")

# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->