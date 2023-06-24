# test for updating DNS, modified from the cloudflare example

import CloudFlare

def main():
    cf = CloudFlare.CloudFlare(token="lol")
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']

        dns_records = cf.zones.dns_records.get(zone_id)

        for record in dns_records:
            if record["name"] == "sylkos.xyz" and record["type"] == "A":
                print(record)

                record["content"] = "198.168.0.1"
                cf.zones.dns_records.put(zone_id, record["id"], data=record)

if __name__ == '__main__':
    main()