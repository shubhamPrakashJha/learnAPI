import requests
# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {
    "lat": 37.78,
    "lon": -122.41
}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

print("======================================================================")
# Get the response data as a python object.  Verify that it's a dictionary.
print(type(response.content))
print(response.content)

print("======================================================================")

data = response.json()
print(type(data))
print(data)

print("======================================================================")

# Headers is a dictionary
print(type(response.headers))
print(response.headers)

# Get the content-type from the dictionary.
print(response.headers["Server"])