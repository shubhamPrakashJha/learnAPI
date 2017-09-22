import requests

response = requests.get("http://api.open-notify.org/iss-now.json")#200 - connnection OK
print(response.status_code)
print(response.content)