import requests
import json

# Set up connection parameters in dictionary
router = {'host':'ios-xe-mgmt.cisco.com','port':9443,
          'username':'developer','password':'C1sco12345'}

# Set REST API Headers
header = {'Accept':'application/yang-data+json',
          'Content-Type':'application/yang-data+json'}

url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

# SEND GET Request and save it to variable response;'
response = requests.get(url, headers=header, auth=(router['username'], router['password']), verify=False)

print(response)
print(response.json())