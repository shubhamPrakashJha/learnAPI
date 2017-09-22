import  requests

response = requests.get("http://api.open-notify.org/iss-pass.json")#400 - sufficiant argument not sent
print(response.status_code)