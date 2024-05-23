# cloudflare-ddns

> ⚠️⚠️⚠️ This project has been rewritten in [sylk0s/simple-ddns](https://github.com/sylk0s/simple-ddns). This was a project I did for a class, and thus, was bad.

A Dynamic DNS script for cloudflare

All the other ones I could find were really old so i just made my own

# Usage
You can either specity the config in a .env file like this:
```
TOKEN=CLOUDFLARE_API_TOKEN_FROM_THEIR_WEBSITE
ZONE=YOUR_DOMAIN_NAME
FREQ=TIME_BETWEEN_UPDATED_IN_MINUTES
TYPE=A_OR_AAAA_DEPENDING_ON_THE_RECORD
DOMAIN=SUBDOMAIN_TO_REDIRECT
```
or using ENV vars directly. I also have a dockerfile and so `build_docker.sh` will generate and run an image (rn it pulls the token from a `token` file and is pointed to my domain, but this could easily be updated... You could also just as easily just take the commands from this file and run them yourself. For the `TYPE`, `A` is the default, and for `FREQ`, `1` minute is the default, but both of these could be changed using the `-e` arg in `docker run`

I basically just use this to keep my domain pointed at my server which has a dynamic IP. 
It's basically just keeping the root for my domain pointed at the server and all the other ones refer to this one main record so everything is updated

Right now it's basically meant just for a single domain, but it's meant to be written in an expandible manner for multiple jobs.
