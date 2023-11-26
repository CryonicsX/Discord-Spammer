# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
import requests, time, pyppeteer, random, jwt, asyncio, json, traceback, base64, yaml
from pyppeteer_ghost_cursor import path
from pyppeteer import launch



class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"
    BLUE = '\033[96m'

config = json.loads(open("./config/config.json", "r", encoding="utf-8").read())

class solver:
    
    def __init__(self, site_key: str, website_url: str, proxyless: bool, proxy: dict = None, useragent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.70 Whale/3.13.131.27 Safari/537.36", rqdata: str = None) -> None:
        self.nocaptcha_api = {"uid": config["nocaptcha_api"]["uid"], "apikey": config["nocaptcha_api"]["apikey"], "solver": "https://free.nocaptchaai.com/api/solve"}
        self.site_key = site_key
        self.siteurl = website_url
        self.motiondata = None
        self.hsw = None
        self.session = requests.Session()
        self.useragent = useragent
        self.rqdata = rqdata
        
        if proxyless:
            self.session.proxies.update(proxy)
            print("upp")

        try:
           self.hcaptcha_version = self.session.get('https://hcaptcha.com/1/api.js?render=explicit&onload=hcaptchaOnLoad').text.split("assetUrl")[1].split("https://newassets.hcaptcha.com/captcha/v1/")[1].split("/static")[0]
        except:
            self.hcaptcha_version = '1f7dc62'


    def get_cap(self):

        headers = {'Authority': "hcaptcha.com", 'Accept': "application/json", "Accept-Language": "en-US,en;q=0.9", "Content-Type": "application/x-www-form-urlencoded", 'Origin': "https://newassets.hcaptcha.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "User-Agent": self.useragent}

        payload = {
            'v': self.hcaptcha_version,
            'host': self.siteurl,
            'sitekey': self.site_key,
            'sc': '1',
            'swa': '1',
        }

        __reqdata__ = self.session.post(f"https://hcaptcha.com/checksiteconfig?v={self.hcaptcha_version}&host={self.siteurl}&sitekey={self.site_key}&sc=1&swa=1", data=payload, headers=headers).json()
        #print(__reqdata__)
        loop = asyncio.new_event_loop()
        hsw, version = loop.run_until_complete(self.get_hsw(__reqdata__['c']['req']))
        self.hsw = hsw

        payload_2 = {
            "v": f"https://hcaptcha.com/getcaptcha/{self.site_key}",
            "sitekey": str(self.site_key),
            "host": str(self.siteurl),
            "hl": "en",
            "motionData": json.dumps(self.generate_motiondata()),
            "n": hsw,
            "c": json.dumps(__reqdata__['c']),
            "rqdata": self.rqdata
        }

        __rqdata__ = self.session.post(f"https://hcaptcha.com/getcaptcha/{self.site_key}", data=payload_2, headers=headers).json()
        return [__rqdata__, __reqdata__]


    def generate_motiondata(self):
        start = {'x': 100, 'y': 100}
        end = {'x': 600, 'y': 700}
        mm = [[int(p['x']), int(p['y']), int(time.time() * 1000) + round(random.random() * (5000 - 2000) + 2000)] for p in path(start, end)]
        timestamp = int((time.time() * 1000) + round(random.random() * (120 - 30) + 30))
        return {'st': timestamp, 'dct': timestamp, 'mm': mm}


    async def get_hsw(self, resp = None):
        url = jwt.decode(resp, options={"verify_signature": False})['l']
        version = url.split("https://newassets.hcaptcha.com/c/")[1]
        hsw = self.session.get(f"{url}/hsw.js").text
    
        time.sleep(2)
        count = 0
        while count <= 3:
            try:
                browser = await launch({"headless": True}, handleSIGINT=False, handleSIGTERM=False, handleSIGHUP=False)
                page = await browser.newPage()
                await page.addScriptTag({'content': hsw})
                resp = await page.evaluate(f'hsw("{resp}")')
                #print(resp)
                await browser.close()
                return resp, version
            except:
                traceback.print_exc()
                try:
                    await browser.close()
                except:
                    pass
                count += 1


    def __answers__(self, data) -> dict:
        i = {}
        t_ = {}
        z = 0
        
        headers = {'Authority': "hcaptcha.com", 'Accept': "application/json", "Accept-Language": "en-US,en;q=0.9", "Content-Type": "application/x-www-form-urlencoded", 'Origin': "https://newassets.hcaptcha.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "User-Agent": self.useragent}
        
        for u in data["tasklist"]:
            img_base64 = base64.b64encode(requests.get(str(u["datapoint_uri"]), headers = headers).content)
            img_base64_decoded = img_base64.decode('utf-8') 
            url = img_base64_decoded
            task_key = str(u["task_key"])
            i[z] = url
            t_[url] = task_key
            z += 1
        g = data["requester_question"]["en"]
        #print(g)
        payload = {
            "images": i,
            "target": g,
            "method": "hcaptcha_base64",
            "site": self.siteurl,
            "sitekey": self.site_key
        }

        headers = {
            "Content-type": "application/json",
            "uid": self.nocaptcha_api["uid"],
            "apikey": self.nocaptcha_api["apikey"]
        }
        
        task_result = requests.post(f"{self.nocaptcha_api['solver']}", json=payload, headers=headers).json()
        #print(task_result)
        status = "new"
        
        if task_result['status'] == 'new':
            url = task_result["url"]
            p2 = None
            z = 0
            answer = {}
            time.sleep(1.5)

            while True:
                p2 = requests.get(url).text
                if "solved" in p2:
                    p2 = json.loads(p2)
                    status = "solved"
                    break
                
                elif not "queue" in p2:
                    return False

                if z >= 5:
                    print(p2)
                    return False

                z += 1
                time.sleep(5)
            
            for d in i:
                if str(d) in p2["solution"]: 
                    answer[t_[i[d]]] = "true"
                    #print("true")
                else: 
                    #print("false")
                    answer[t_[i[d]]] = "false"
        
        elif task_result['status'] == 'solved':
            answer = {}
            status = 'solved'
            for d in i:
                if d in task_result["solution"]: 
                    answer[t_[i[d]]] = "true"
                else: 
                    answer[t_[i[d]]] = "false"

        if status == "solved":
            #print(answer)
            return answer



    def solve(self) -> str:
        c = self.get_cap()
        rqdata = c[0]
        reqdata = c[1]
        key, tasklist = rqdata["key"], rqdata["tasklist"]
        time.sleep(1.5)

        loop = asyncio.new_event_loop()
        hsw, version = loop.run_until_complete(self.get_hsw(reqdata['c']['req']))

        payload = {
            "v": self.hcaptcha_version,
            "job_mode": "image_label_binary",
            "answers": self.__answers__(rqdata),
            "serverdomain": f'{self.siteurl}',
            "sitekey":f'{self.site_key}',
            "motionData": json.dumps(self.generate_motiondata()),
            "n": json.dumps(hsw),
            "c": "{\"type\":\"" + reqdata["c"]["type"] + "\",\"req\":\"" + reqdata["c"]["req"] + "\"}"
            }
        
        
        headers = {
                "Authority": "hcaptcha.com",
                "content-type": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "content-length": str(len(payload)),
                "accept": "*/*",
                "origin": "https://newassets.hcaptcha.com",
                "referer": "https://newassets.hcaptcha.com/",
                "user-agent": self.useragent,
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site"
        }
        submit_captcha = self.session.post(f"https://hcaptcha.com/checkcaptcha/{self.site_key}/{key}", json=payload, headers=headers).json()
        #print(submit_captcha)

        if "generated_pass_UUID" in submit_captcha:
            token = submit_captcha["generated_pass_UUID"]
            #print(f"{color.GREEN}[+] CAPTCHA SOLVED {token[:39]}.....{token[-39:]} {color.RESET_ALL}")
            return submit_captcha["generated_pass_UUID"]
        else:
            print(f"{color.RED}[-] Images Incorrectly Recognized {color.RESET_ALL}")
            return 'Images Incorrectly Recognized'
        

#solver("4c672d35-0701-42b2-88c3-78380b0db560", "discord.com", False).solve()

# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->