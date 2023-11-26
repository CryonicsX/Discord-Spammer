# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->

import requests, threading

working_proxies = []
error = None


def proxy_appender(proxy_url: str, proxy_protocol: str) -> None:
    global error

    proxies = None

    if proxy_protocol == 'HTTP':
        proxies = {
            'http': f"http://{proxy_url}",
            'https': f"http://{proxy_url}"
        }
    elif proxy_protocol == 'SOCKS4':
        proxies = {
            'http': f"socks4://{proxy_url}",
            'https': f"socks4://{proxy_url}"
        }
    elif proxy_protocol == 'SOCKS5':
        proxies = {
            'http': f"socks5://{proxy_url}",
            'https': f"socks5://{proxy_url}"
        }

    else:
        error = 'Invalid proxy protocol.'

    try:
        a = requests.get("http://ip-api.com/json/", proxies=proxies, timeout=10, verify=False)
        working_proxies.append(proxies["http"].split("//")[1])
    except:
        pass


class Proxy:
    def __init__(self, config):
        self.config = config

    def check_proxies(self) -> list:
        global error, working_proxies

        with open(f'./config/proxies.txt') as file:
            proxies = [line.rstrip() for line in file.readlines()]


        threads = []
        for proxy_url in proxies:
            t = threading.Thread(target=proxy_appender, args=(proxy_url, self.config["proxy_protocol"],))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        if error:
            return [False, error]

        if len(working_proxies) == 0:
            return [False, 'Proxies not working. Please fill proxies.txt with new proxies.']

        return [True, working_proxies, len(working_proxies)]

# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->
# <---- Developed by CryonicX1337 ----->