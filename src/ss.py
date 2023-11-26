# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->

import requests, time, re
from pyppeteer import launch
from .cf import claudflare

class HttpSession:
    def __init__(self, proxy: dict = None, user_agent: str = None, auth_token: str = None) -> None:
        response = requests.get("http://fingerprints.bablosoft.com/preview?rand=0.1&tags=Firefox,Desktop,Microsoft%20Windows").json()

        self.base_headers = {
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Origin": "https://discord.com",
            "authorization": auth_token,
            'User-Agent': response["ua"],
            'accept-language': f"en-US",
            'accept-encoding': 'gzip, deflate',
            'content-type': 'application/json',
            'referer': '',
            'origin': '',
            'sec-fetch-site': 'same-origin',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'accept': '*/*',
            "href": ""
        }

        self.session = requests.Session()
        
        if proxy:
            self.session.proxies.update(proxy)
            print("PROXY USED")

        self.headers = self.session.headers
        self.session.headers.update(self.base_headers)

    def get_cookies(self):
        cookies = self.session.cookies
        cookies.clear()

        cf_params = claudflare.get_cf(self.session)
        r, m, __cfruid, __dcfduid, __sdcfduid, htmltext = cf_params[0], cf_params[1], cf_params[2], cf_params[3], cf_params[4], cf_params[5]

        cookies.set("__dcfduid", __dcfduid, domain="discord.com")
        cookies.set("__sdcfduid", __sdcfduid, domain="discord.com")
        cookies.set("__cfruid", __cfruid, domain="discord.com")
        cookies.set("locale", "en-US", domain="discord.com")


        self.session.headers["cookies"] = f"__dcfduid={__dcfduid}; __sdcfduid={__sdcfduid}; __cfruid={__cfruid};"

        Js = self.session.get(f"https://discord.com/cdn-cgi/challenge-platform/scripts/invisible.js").text

        Kw = Js.split("{a='")[0].split("'.split(';')")[0].split(";")
        for K in Kw:
            if len(K) == 65:
                Pass = K

            
        Nonce = htmltext.split("_cpo.nonce='")[1].split(",_cpo.src='")[0].split(";")[0].split("'")[0]
        Base = re.findall('[0-9]*.[0-9]+:[0-9]+:',Js)

        S = f"{Base[0]}{Js.split(Base[0])[1][:43]}"

        paylaod = {
            "Nonce": Nonce,
            "S": S,
            "Password": Pass
        }

        __cf_bm = claudflare.get_cookie(self.session, r, m, paylaod)
        
        """
        if len(__cf_bm) == 189:
            print("Flagged: False")
        else:
            print("Flagged: True")
        """

        #print(len(__cf_bm))
        cookies.set("__cf_bm", __cf_bm, domain="discord.com")
        cookies.get("locale", "en-GB", domain="discord.com")

        self.session.headers["cookies"] = f"__dcfduid={__dcfduid}; __sdcfduid={__sdcfduid}; __cfruid={__cfruid}; __cf_bm={__cf_bm}, locale=en-GB"



    async def get_cookies_browser(self):
        cookies = self.session.cookies
        cookies.clear()
        
        browser = await launch({"headless": False})

        # Open a new page in the browser
        page = await browser.newPage()
        print("opened")

        # Navigate to a website
        await page.goto('https://discord.com/')
        await page.goto("https://discord.com/login")

        time.sleep(10)
        # Get the cookies for the current page
        cookies = await page.cookies()

        # Close the browser
        await browser.close()

        # Print the cookies to the console
        print(cookies)

        __dcfduid = cookies[0]["value"]
        _gcl_au = cookies[1]["value"]
        _gat_UA_53577205_2 = cookies[2]["value"]
        __cfruid = cookies[3]["value"]
        OptanonConsent = cookies[4]["value"]
        _gid = cookies[5]["value"]
        locale = cookies[6]["value"]


# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->