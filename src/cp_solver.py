import requests 

class solver_:

    def __init__(self, apikey: str) -> None:
        self.apikey = apikey


    def create_task(self, rqdata: str, websiteURL: str, websiteKey: str, useragent: str, proxy: str = None):


        payload = {
                "clientKey": self.apikey,
                "task": {
                    "type": "HCaptchaTaskProxyLess",
                    "websiteURL": websiteKey,
                    "websiteKey": websiteURL,
                    
                    "enterprisePayload": {
                        "rqdata": rqdata
                    },

                    "userAgent": useragent
                }
        }

        if proxy is None:
            payload = {
                "clientKey": self.apikey,
                "task": {
                    "type": "HCaptchaTaskProxyLess",
                    "websiteURL": websiteKey,
                    "websiteKey": websiteURL,
                    
                    "enterprisePayload": {
                        "rqdata": rqdata
                    },

                    "userAgent": useragent,
                    "proxy": proxy,
                }
            }

        

        response = requests.post("https://api.capsolver.com/createTask", json=payload)

        if response.json()["errorId"] == 0:
            return response.json()["taskId"]
        
        else:
            return response.json()["errorDescription"]
        


    def get_result(self, task_id: str):
        
        payload = {
            "clientKey": self.apikey,
            "taskId": task_id
        }

        x = True
        while x:
            response = requests.post("https://api.capsolver.com/getTaskResult", json=payload)
            if response.json()["status"] == "ready":
                x = False


            return response.json()["gRecaptchaResponse"]

    