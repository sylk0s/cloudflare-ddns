import runner
import requests
import CloudFlare

from runner import Runnable

# gets the current IP
class IPGetter:
    def get_my_ip():
        response = requests.get("https://api.my-ip.io/ip.json").json()
        #print("ip is:", response["ip"])
        return response["ip"], response["type"]

# handles cloudflare IO & API calls
class ClfIO:
    record_map = {
        "IPv4":"A",
        "IPv6":"AAAA",
    }

    def __init__(self, token):
        self.cf = CloudFlare.CloudFlare(token=token)
        
    def update_record(self, record_type, domain, zone, prev_ip):
        #print("attempting update...")
        # for each zone
        zones = self.cf.zones.get()
        for z in zones:
            zone_id = z["id"]
            zone_name = z["name"]
            
            # if this is the correct zone, try to update the dns
            if zone_name == zone:
                dns_records = self.cf.zones.dns_records.get(zone_id)
                #print("found zone...")

                # for each record determine if it's the right record
                for record in dns_records:
                    if self.is_correct_record(record, record_type, domain):

                        # updates the record obj with the new ip if it's the right type
                        new_ip, ip_type = IPGetter.get_my_ip()
                        
                        #print(f"{self.type_match_record(ip_type, record_type)} | {not new_ip == prev_ip}")
                        if self.type_match_record(ip_type, record_type) and not new_ip == prev_ip:
                            record["content"] = new_ip
                            self.cf.zones.dns_records.put(zone_id, record["id"], data=record)
                            #print(f"record updated as {record}")
                            return new_ip

    def type_match_record(self, iptype, record):
        return self.record_map[iptype] == record

    def is_correct_record(self, record, record_type, domain):
        return  record["name"] == domain and record["type"] == record_type

# job which when run, updates the record
class DynDNSJob(Runnable):
    def __init__(self, config):
        super().__init__(config.freq)
        self.config = config
        self.clf = ClfIO(config.token)
        self.prev_ip = None
        self.run()


    def run(self):
        #print("running ddns")
        result = self.clf.update_record(self.config.record_type, self.config.domain, self.config.zone, self.prev_ip)
        if result is not None:
            self.prev_ip = result