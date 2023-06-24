import runner
import requests
import CloudFlare

from runner import Runnable


# gets the current IP
class IPGetter:
    """
    A class to handle getting the IP
    """

    # I made this a class because at some point, i plan to update this to store metadata of some sort so we can query
    # this website less or handle any 4XX or 5XX error gracefully, since i feel kinda bad spamming their API every minute

    def get_my_ip():
        """Gets the current public IP of the local machine"""

        response = requests.get("https://api.my-ip.io/ip.json").json()
        #print("ip is:", response["ip"])
        return response["ip"], response["type"]


class ClfIO:
    """
    Handles IO with cloudflare's API
    """

    # map of IP type to the record it should update
    # hopefully this will work with IPv6 but IDK how to actually test that
    record_map = {
        "IPv4":"A",
        "IPv6":"AAAA",
    }


    def __init__(self, token):
        """Creates a CloudFlare API object"""

        self.cf = CloudFlare.CloudFlare(token=token)
        

    def update_record(self, record_type, domain, zone, prev_ip):
        """Updates the specified DNS record. Returns either None or the new IP"""

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
                        # if the record types match and the IPs are different, then update the IP
                        if self.type_match_record(ip_type, record_type) and not new_ip == prev_ip:
                            record["content"] = new_ip
                            self.cf.zones.dns_records.put(zone_id, record["id"], data=record)
                            #print(f"record updated as {record}")
                            return new_ip


    def type_match_record(self, iptype, record):
        """Determines if an IP type matches the desired record"""

        return self.record_map[iptype] == record


    def is_correct_record(self, record, record_type, domain):
        """Determines if a record is desired record"""

        return  record["name"] == domain and record["type"] == record_type


class DynDNSJob(Runnable):
    """
    A job which keeps some DNS record pointed at the current machine's public IP
    """

    
    def __init__(self, config):
        """sets up this job from the config"""

        super().__init__(config.freq)
        self.config = config
        self.clf = ClfIO(config.token)
        self.prev_ip = None
        self.run()


    def run(self):
        """Runs this job"""

        #print("running ddns")
        result = self.clf.update_record(self.config.record_type, self.config.domain, self.config.zone, self.prev_ip)

        # updates this job with the new current IP if it changes
        if result is not None:
            self.prev_ip = result