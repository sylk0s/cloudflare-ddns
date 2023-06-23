import CloudFlare

def main():
    cf = CloudFlare.CloudFlare(token="lol")
    zones = cf.zones.get()
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        print("zone_id=%s zone_name=%s" % (zone_id, zone_name))

if __name__ == '__main__':
    main()