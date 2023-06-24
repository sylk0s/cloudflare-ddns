docker build --tag cloudflare-ddns .
docker run -d -e TOKEN=$(cat token) -e ZONE=sylkos.xyz -e DOMAIN=sylkos.xyz --name clf_ddns cloudflare-ddns