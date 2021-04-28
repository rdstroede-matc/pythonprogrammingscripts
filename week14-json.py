#!/usr/bin/env python3
import sys
import requests
import json
import argparse

parser = argparse.ArgumentParser(description="This is the description of your script")
ip = ''
#================== Add arguments=============================================

##### Most Basic Example
parser.add_argument('-ip', dest='ip', help='Please enter in an IP.')
ip = parser.parse_args().ip

# Create the url that we want to connect to
url = f"http://ipinfo.io/{ip}/json"

# Send the “get” request to the web server
jsonResp = requests.get(url)
# Convert the returned json formatted text to a dictionary
print(url)
print(jsonResp)
myDict = json.loads(jsonResp.text)

# for each key in the dictionary print the key and the data
for key in myDict.keys():
    print(f"{key: <10}:{myDict[key]: <10}")


