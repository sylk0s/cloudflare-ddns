import runner
import requests


# handles cloudflare IO & API calls
class ClfIO:

    def __init__(self, config):
        self.config = config
        self.cf = CloudFlare.CloudFlare(token=self.config.get_token())
        
    def update_record(self):
        pass

# job which when run, updates the fairs
class DynDNSJob(Runnable):


    def run(self):
        pass

# gets the current IP
class IPGetter:
    def get_my_ip():
        response = requests.get("https://api.my-ip.io/ip.json").json()
        return response["ip"], response["type"]