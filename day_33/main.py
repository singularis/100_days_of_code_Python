import requests

responce = requests.get(url='http://api.open-notify.org/iss-now.json')
print(responce)