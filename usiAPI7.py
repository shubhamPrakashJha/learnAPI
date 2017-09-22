import requests

# Get the response from the API endpoint.
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space.
print(data)
print(data["number"])
print(data["people"])

arr_of_people = data["people"]
# print(arr_of_people[0]['name'])
for astronomer in arr_of_people:
    print("astronomer: "+astronomer['name'])
    print("Craft: "+astronomer['craft'])
    print('-----------------------------------')
