import json
import os


def short_link():
    url = input("enter url: ")
    short_name = input("enter short name: ")

    if short_name in short_links:
        print("name already in use")
    else:
        short_links[short_name] = url
        with open('links.json', 'w') as f:
            json.dump(short_links, f, indent=4)

def get_old_link():
    short_name = input("enter short name: ")
    if short_name in short_links:
        print(f"original name: {short_links[short_name]}")
    else:
        print("not found")

def get_all_names():
    with open('links.json', 'r') as f:
        print(json.load(f))

file = 'links.json'

if os.path.exists(file):
    with open(file, 'r') as f:
        short_links = json.load(f)
else:
    open(file, 'x').close()
    short_links = {}