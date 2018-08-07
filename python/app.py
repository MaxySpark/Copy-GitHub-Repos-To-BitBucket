import requests
import argparse
import json
parser = argparse.ArgumentParser()
parser.add_argument("username", help="Github Username")
parser.add_argument("password", help="Github Password")
args = parser.parse_args()
# print(args.username)

username = args.username or ""
password = args.password or ""

r = requests.get('https://api.github.com/user/repos', auth=(username, password))
# print(r)
# print(r.json())
# print(json.dumps(r.json()))

for repo in r.json():
    print(repo["git_url"])

# print(json.dumps(r.json()))