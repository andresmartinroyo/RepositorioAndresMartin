import requests

response = requests.get("https://www.google.com/?hl=es")
print(response)
print(response.content)