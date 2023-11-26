# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->

import requests, re, json, random, websocket, threading, discum, sys, base64, time
from user_agents import parse

#from .solver import *
from .cp_solver import solver_



sys.setrecursionlimit(1500)
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
    RESET_ALL = '\033[0m'
    BACK = '\033[1A'

class member_scraper:
    def __init__(self, token: str) -> None:
        self.token = token
        self.bot = discum.Client(token=self.token, log=False)

    def close_after_fetching(self, resp, guild_id):
        bot = self.bot
        if bot.gateway.finishedMemberFetching(guild_id):
            lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
            print(f"{color.GREEN}[MEMBER_SCRAPER]{color.RESET_ALL} {lenmembersfetched} Member fetched from {color.BLUE}[{self.token}]{color.RESET_ALL}")
            bot.gateway.removeCommand({'function': self.close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()

    def get_members(self, guild_id, channel_id):
        bot = self.bot
        bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
        bot.gateway.command({'function': self.close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guild_id).members




class DiscordWs(threading.Thread):
    def __init__(self, acc_token: str, useragent: str) -> None:
        self.token = acc_token
        self.useragent = useragent
        self.running = True
        self.ws = websocket.WebSocket()
        threading.Thread.__init__(self)

    def send_payload(self, payload: dict) -> None:
        print(f"{color.YELLOW}[websocket]{color.RESET_ALL} dump -> {payload}")
        self.ws.send(json.dumps(payload))

    def recieve(self) -> dict:
        data = self.ws.recv()

        if data:
            return json.loads(data)

    def heartbeat(self, interval: float):
        while self.running:
            time.sleep(interval)
            self.send_payload({
                'op': 1,
                'd': None
            })

    def login(self):
        self.ws.connect('wss://gateway.discord.gg/?encoding=json')
        interval = self.recieve()['d']['heartbeat_interval'] / 1000
        threading.Thread(target=self.heartbeat, args=(interval,)).start()


    def open_channel(self, channel_link: str):
        self.send_payload(
            {
                "op":13,
                "d":{
                        "channel_id": channel_link
                    }
            }
        )

    def join_guild(self, guild_id: str, channel_id: str):
        self.send_payload(
            {
                "op": 14,
                "d" : {
                    "guild_id": guild_id,
                    "typing": True,
                    "activities": True,
                    "threads": True,
                    "channels": {
                        f"{channel_id}": [[0,99]]
                    }

                }
            }
        )

    def online(self):
        user_agent = parse(self.useragent)
        self.send_payload({
            "op": 2,
            "d": {
                
                "token": self.token,
                "capabilities": 509,
                
                "client_state": {
                    "guild_hashes": {},
                    "highest_last_message_id": "0",
                    "read_state_version": 0,
                    "user_guild_settings_version": -1,
                    "user_settings_version": -1
                },
                
                "compress": False,

                "presence": {
                    "status": "online",
                    "since": 0,
                    "activities": [],
                    "afk": False
                },
                
                "properties": {
                    "os": str(user_agent.os.family),
                    "os_version": str(user_agent.os.version_string),
                    "browser": str(user_agent.browser.family),
                    "browser_user_agent": self.useragent,
                    "device":str(user_agent.device.model),
                    "referrer": "",
                    "referring_domain":"",
                    "release_channel":"stable",
                    "client_build_number":142868, 
                    "client_event_source": None,
                    "system_locale": "en-GB"
                }
            }
        })

        time.sleep(6)

        self.send_payload({
            "op": 3,
            "d": {
                "status": random.choice(["online", "idle", "dnd"]),
                "since": 0,
                "activities": [
                    {
                        "name": "Custom Status",
                        "type": 4,
                        "state": "",
                        "emoji": None
                    }
                ],
                "afk": False
            }
        })

    def run(self):
        self.login()
        self.online()
        #time.sleep(30)
        self.running = False



    
class discord_api:
    def __init__(self, session, api_version: str = "9", use_websocket: bool = False) -> None:
        
        self.session = session
        self.api_version = api_version
        self.session.headers["x-super-properties"] = self.get_trackers()
        self.session.headers["x-debug-options"] = "bugReporterEnabled"
        self.session.headers["x-discord-locale"] = "en-US"
        self.ws = False

        if use_websocket:
            try:
                self.ws = DiscordWs(self.session.headers['authorization'], self.session.headers["user-agent"])
                threading.Thread(target=self.ws.run, args=()).start()
                #print("ws connected")
            except Exception as e:
                print(e)

        #print(self.ws)

    def get_trackers(self):
        user_agent = parse(self.session.headers["user-agent"])
        payload = {
                #"vendor": vendor,
                "os": str(user_agent.os.family),
                "browser": str(user_agent.browser.family),
                "device":str(user_agent.device.model),
                "system_locale":"en-US",
                "browser_user_agent":self.session.headers["user-agent"],
                "browser_version":str(user_agent.browser.version_string),
                "os_version": str(user_agent.os.version_string),
                "referrer": "",
                "referring_domain":"",
                "referrer_current":"",
                "release_channel":"stable",
                "client_build_number": 156904,
                "client_event_source":None
        }

        return base64.b64encode(json.dumps(payload, separators=(',', ':')).encode()).decode()


    def send_directmessage(self, target_id: str, content: str):

        self.session.headers["content-type"] = "application/json"

        check_user = self.session.get(f"https://discord.com/api/v{self.api_version}/users/{target_id}/profile?with_mutual_guilds=true")
        #print(check_user.json())

        if check_user.status_code == 200:

            print(f"{color.GREEN}[{check_user.json()['user']['username']}#{check_user.json()['user']['discriminator']}]{color.RESET_ALL} User found from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
            
            self.session.headers["referer"] = f"https://discord.com/channels/@me/{target_id}"
            
            time.sleep(1.5)


            payload = {
                "recipient_id": target_id
            }
            
            open_channel = self.session.post(f"https://discord.com/api/v{self.api_version}/users/@me/channels", json=payload)

            
            
            if open_channel.status_code == 200:
                
                if self.ws:
                    self.ws.open_channel(channel_link=open_channel.json()['id'])


                if open_channel.status_code == 200:

                    time.sleep(1.5)

                    username = f"{open_channel.json()['recipients'][0]['username']}#{open_channel.json()['recipients'][0]['discriminator']}"
                    
                    if "<user>" in content:
                        new_c = f"<@{target_id}>"
                        content = content.replace("<user>", new_c)

                    payload = {
                        "content": content,
                        "tts": False,
                        "nonce": open_channel.json()["id"]
                    }


                    self.session.headers["content-length"] = str(len(str(payload)))

                    send_message = self.session.post(f"https://discord.com/api/v{self.api_version}/channels/{open_channel.json()['id']}/messages", json=payload)

                    if "captcha_key" not in send_message.text:
                        
                        if send_message.status_code == 200:
                            print(f"{color.GREEN}[{username}]{color.RESET_ALL} Message sent from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
                        
                        else:
                            print(f"{color.RED}[{username}]{color.RESET_ALL} Message cant send from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {send_message.json()}")

                    else:
                        print(f"{color.YELLOW}[{username}]{color.RESET_ALL} Captcha dedected from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

                        
                        #c = solver(send_message.json()['captcha_sitekey'], "discord.com", False, None, self.session.headers["user-agent"], send_message.json()["captcha_rqdata"]).solve()
                        
                        task = solver_(config["capsolver"]["apikey"]).create_task(send_message.json()["captcha_rqdata"], "discord.com", send_message.json()['captcha_sitekey'], self.session.headers["user-agent"], False)

                        print(task)

                        c = solver_(config["capsolver"]["apikey"]).get_result(task)

                        print(f"{color.GREEN}[{username}]{color.RESET_ALL} Captcha solved from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {c[:39]}.....{c[-39:]}")
                        
                        payload = {
                            "captcha_key": c,
                            "captcha_rqtoken": send_message.json()['captcha_rqtoken'],
                            "content": content,
                            "tts": False,
                            "nonce": open_channel.json()["id"],
                        }

                        send_message = self.session.post(f"https://discord.com/api/v{self.api_version}/channels/{open_channel.json()['id']}/messages", json=payload)

                        if send_message.status_code == 200:
                            print(f"{color.GREEN}[{username}]{color.RESET_ALL} Message sent from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
                        
                        else:
                            print(f"{color.RED}[{username}]{color.RESET_ALL} Message cant send from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {send_message.json()}")

            else:
                print(f"{color.RED}[!]{color.RESET_ALL} Channel cant open from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
                return False

        else:
            print(f"{color.RED}[!]{color.RESET_ALL} User Cant found from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
            return False 

    def join_guild(self, invite_code: str):
        get_guild = self.session.get(f"https://discord.com/api/v{self.api_version}/invites/{invite_code}")


        if get_guild.status_code == 200:

            print(f"{color.GREEN}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Guild Found from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")


            join_guild = self.session.post(f"https://discord.com/api/v{self.api_version}/invites/{invite_code}", json={})

            if "captcha_key" not in join_guild.text:
                if join_guild.status_code == 200:
                
                    print(f"{color.GREEN}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Guild joined from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

                else:
                    print(f"{color.RED}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Guild cant joined from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {join_guild.json()}")

            else:
                print(f"{color.YELLOW}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Captcha dedected from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

                #c = solver(join_guild.json()['captcha_sitekey'], "discord.com", False, None, self.session.headers["user-agent"], join_guild.json()["captcha_rqdata"]).solve()

                task = solver_(config["capsolver"]["apikey"]).create_task(send_message.json()["captcha_rqdata"], "discord.com", send_message.json()['captcha_sitekey'], self.session.headers["user-agent"], False)

                print(task)

                c = solver_(config["capsolver"]["apikey"]).get_result(task)


                print(f"{color.GREEN}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Captcha solved from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {c[:39]}.....{c[-39:]}")

                payload = {
                    "captcha_key": c,
                    "captcha_rqtoken": join_guild.json()['captcha_rqtoken']
                }

                join_guild = self.session.post(f"https://discord.com/api/v{self.api_version}/invites/{invite_code}", json=payload)

                if join_guild.status_code == 200:
                    print(f"{color.GREEN}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Guild joined from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
                else:
                    print(f"{color.RED}[{get_guild.json()['guild']['name']}]{color.RESET_ALL} Guild cant joined from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {join_guild.json()}")


        else:
            print(f"{color.RED}[-]{color.RESET_ALL} Guild cant checked from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {get_guild.json()}")


                    
    def left_guild(self, guild_id: str):

        left_g = self.session.delete(f"https://discord.com/api/v{self.api_version}/users/@me/guilds/{guild_id}", json={"lurking": False})

        if left_g.status_code == 204:
            print(f"{color.GREEN}[{guild_id}]{color.RESET_ALL} Guild Left from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

        else:
            print(f"{color.RED}[{guild_id}]{color.RESET_ALL} Guild cant left from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {left_g.json()}")



    def avatar_changer(self, avatar_url: str):

        payload  = {
            "avatar": "data:image/png;base64," + base64.b64encode(requests.get(avatar_url).content).decode("utf-8") + "="
        }
        time.sleep(3)
        ca_ = self.session.patch(f"https://discord.com/api/v{self.api_version}/users/@me", json=payload)

        if ca_.status_code == 200:
            print(f"{color.GREEN}[{ca_.json()['username']}#{ca_.json()['discriminator']}]{color.RESET_ALL} Avatar changed from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

        else:
            print(f"{color.RED}[AVATAR]{color.RESET_ALL} Avatar cant changed from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {ca_.json()}")



    def friend_requester(self, user: str):

        payload = {
            "discriminator": user.split("#")[1],
            "username": user.split("#")[0]
        }
        
        res = self.session.post(f"https://discord.com/api/v{self.api_version}/users/@me/relationships", json=payload)
        
        if "captcha_key" not in res.text:
            
            if res.status_code == 204:
                print(f"{color.GREEN}[{user}]{color.RESET_ALL} User added from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
            else:
                print(f"{color.RED}[{user}]{color.RESET_ALL} User cant added from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {res.json()}")

        else:
            print(f"{color.YELLOW}[{user}]{color.RESET_ALL} Captcha dedected from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

            c = solver(res.json()['captcha_sitekey'], "discord.com", False, None, self.session.headers["user-agent"], res.json()["captcha_rqdata"]).solve()

            print(f"{color.GREEN}[{user}]{color.RESET_ALL} Captcha solved from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {c[:39]}.....{c[-39:]}")

            payload = {
                "captcha_key": c,
                "captcha_rqtoken": res.json()['captcha_rqtoken'],
                "discriminator": user.split("#")[1],
                "username": user.split("#")[0]
            }


            res = self.session.post(f"https://discord.com/api/v{self.api_version}/users/@me/relationships", json=payload)
            
            if res.status_code == 204:
                print(f"{color.GREEN}[{user}]{color.RESET_ALL} User added from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")
            else:
                print(f"{color.RED}[{user}]{color.RESET_ALL} User cant added from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {res.json()}")

    def scrape_members(self, token: str, guild_id: str, channel_id: str, invite_code: str):
        
        j_ = self.join_guild(invite_code)

        members = member_scraper(token).get_members(guild_id, channel_id)
        f = open('./config/users.txt', "a")
        f.truncate(0)
        for memberID in members:
            f.write(memberID + '\n')
            #print(memberID)
        f.close()




    def mass(self, target_id: str, content: str, invite_code: str, guild_id: str):

        self.join_guild(invite_code, guild_id)
        self.send_directmessage(target_id, content)



    def emoji_react(self, channel_id: str, message_id: str, emoji: str):

        #self.join_guild("rmBA2dQu")
        r = self.session.put(f"https://discord.com/api/v{self.api_version}/channels/{channel_id}/messages/{message_id}/reactions/%F0%9F%91%8D/@me?location=Message&burst=false")

        if r.status_code == 204:
            print(f"{color.GREEN}[EMOJI]{color.RESET_ALL} Emoji Reacted from  {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL}")

        else:
            print(f"{color.RED}[EMOJI]{color.RESET_ALL} Emoji cant reacted from {color.BLUE}[{self.session.headers['authorization']}]{color.RESET_ALL} -> {r.json()}")


# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->