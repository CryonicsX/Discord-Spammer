# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->

import requests, random, re, numpy

class claudflare:
    
    def get_cf(session) -> str:
        html = session.get("https://discord.com")
        #print(html.text)
        r = str(re.findall(r"r:'[^']*'", html.text)[0]).replace("r:'", "").replace("'", "")
        m = str(re.findall(r"m:'[^']*'", html.text)[0]).replace("m:'", "").replace("'", "")
        #u = str(re.findall(r"u:'[^']*'", html.text)[0]).replace("u:'", "").replace("'", "")
        #s = str(re.findall(r"s:'[^']*'", html.text)[0]).replace("s:'", "").replace("'", "")
        return r, m, html.cookies["__cfruid"], html.cookies["__dcfduid"], html.cookies["__sdcfduid"], html.text


    def get_fp(password: str):
        
        payload = {
            "pass": password
        }
        
        resp = requests.post("http://127.0.0.1:3000/book", data=payload)
        return resp.text

    
    def get_cookie(session, r: str, m: str, js):
        
        timing = numpy.float64(int(random.uniform(100,400)))


        paylaod = {
            "src": "worker",
            "t": numpy.float64(timing+numpy.float64(int(random.uniform(300, 500))) + random.random()),
            "s": js["S"],
            "fp": {
                "results": [hex(random.getrandbits(16*8))[2:], hex(random.getrandbits(16*8))[2:]],
                "timing": int(timing)
            },
            "m": m,
            "wp": claudflare.get_fp(js["Password"])
        }

        #print(paylaod)

        resp = session.post(f"https://discord.com/cdn-cgi/challenge-platform/h/b/cv/result/{r}", json=paylaod)
        return resp.cookies["__cf_bm"]

# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->