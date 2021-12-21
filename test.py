import requests

BASE_URL = "http://127.0.0.1:5000/"

response = requests.put(BASE_URL + "video/1", {"name" : "ashiap", "likes" : 10, "views" : 10000})
print(response.json())
input()
response = requests.get(BASE_URL + "video/1")
print(response.json())