import requests
import argparse
import json
import pydash as _
parser = argparse.ArgumentParser()
parser.add_argument("username", help="Github Username")
parser.add_argument("password", help="Github Password")
args = parser.parse_args()
# print(args.username)

# if not args.username or not args.password

username = args.username or ""
password = args.password or ""

init_api_url = 'https://api.github.com/user/repos?per_page=100'

repo_data = []

def loop_request(api_url):
    r = requests.get(api_url, auth=(username, password))
    header_links = r.links

    for repo in r.json():
        model = {
            "name"      : repo["name"],
            "git_url"   : repo["git_url"],
            "ssh_url"   : repo["ssh_url"],
            "clone_url" : repo["clone_url"],
            "private"   : repo["private"]
        }
        repo_data.append(model)

    if "next" in header_links:
        loop_request(header_links["next"]["url"])

loop_request(init_api_url)

print(json.dumps(_.filter_(repo_data,{"private":True})))