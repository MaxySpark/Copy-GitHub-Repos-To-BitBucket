import requests

username = ""
password = ""

r = requests.get('https://api.github.com/user', auth=(username, password))
print(r)
print(r.json())