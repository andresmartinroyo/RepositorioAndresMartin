import requests
import json
url = "http://httpbin.org/get"

response = requests.get(url)

#response_json=response.json()
response_json=json.loads(response.text)
origin = response_json["origin"]
print(origin)
print(response_json)