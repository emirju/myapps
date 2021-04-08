from napalm import get_network_driver
import json

driver = get_network_driver('ios')

enable = {'secret': 'automation'}
device = driver('192.168.128.129', 'emir', 'cisco', timeout=60, optional_args=enable)

device.open()

output = device.get_facts()  # method that returns information about devices start with GET

#convert output to a string using JSON module
json_print = json.dumps(output, sort_keys=True ,indent=5)  # output is a list of dictionaries
print(json_print)

device.close()

#### The dumps() is used when the objects are required to be in string format and is used for parsing, printing, etc
#### The dump() method is used when the Python objects have to be stored in a file.