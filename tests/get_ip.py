import requests

response = requests.get("https://api.my-ip.io/ip.json")

result = response.json()

print("My Public IP is:", result["ip"])