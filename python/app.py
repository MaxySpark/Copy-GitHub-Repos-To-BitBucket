import requests
import argparse
import json
import pydash as _
import getpass

parser = argparse.ArgumentParser()
parser.add_argument("--UG", nargs='?' , type=str , help="Github Username")
parser.add_argument("--PG", nargs='?' , type=str , help="Github Password")
args = parser.parse_args()
# print(args.username)

username = args.UG
password = args.PG

if not args.UG:
    username = input("Please Enter Username Of Your Github Account : ")
    username = username.strip(' ')
if not args.PG:
    if username == "":
        print("\n\nERROR!!!!!")
        print("Username Can't Be Empty\n\n")
        quit()
    txt = "Please Enter Password For {i} : ".format(i=username)
    password = getpass.getpass(prompt=txt)
    if password == "":
        print("\n\nERROR!!!!!")
        print("Password Can't Be Empty\n\n")
        quit()

init_api_url = 'https://api.github.com/user/repos?per_page=100'

repo_data = []

def loop_request(api_url):
    r = requests.get(api_url, auth=(username, password))
    header_links = r.links
    
    if "message" in r.json():
        print("\n\nERROR!!!!!")
        print("Something Went Wrong! Please Check Your Github Username and Password and Try Again!\n\n")
        quit()

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

def repo_select(i):
    switcher={
                1 : 'All',
                2 : False,
                3 : True
            }
    return switcher.get(i,"Invalid Selection")

def write_data_to_file(file_name,data):
    with open('outjson.json','w') as fp:
        json.dump({ "data" : data} , fp, indent=4)


print("Choose Repositories Option : \n")
print("     [1] : Get All Repositories\n")
print("     [2] : Get Only Public Repositories\n")
print("     [3] : Get Only Private Repositories\n")
# print("Note : Default is  [1] : Get All Repositories\n")

choice = None
isPrivate = None

while True:
    try:
        choice = int(input("Enter Your Choice : "))
        isPrivate = repo_select(choice)
        
        if isPrivate == "Invalid Selection":
            continue

    except ValueError:
       print("Invalid Selection! Try again.")
       print(isPrivate)
       continue

    else:
        break

loop_request(init_api_url)

if isPrivate != "All":
    print(json.dumps(_.filter_(repo_data,{"private":isPrivate}),indent=4))
    write_data_to_file('outdata.json', (_.filter_(repo_data,{"private":isPrivate })))
else:
    print(json.dumps(repo_data,indent=4))
    write_data_to_file('outdata.json', repo_data )

    

