import requests

response = requests.get("http://api.open-notify.org/iss-pass")#404 - resource not found
print(response.status_code)