from napalm import get_network_driver

cisco_device = get_network_driver('ios')

enable_secret = {'secret': 'automation'}
device = cisco_device('192.168.128.129', 'emir', 'cisco', optional_args=enable_secret)

device.open()

# start the config here ...
output = device.get_users()
print(output)

device.close()

'''  get_users()
Returns a dictionary with the configured users. The keys of the main dictionary represents the username. 
The values represent the details of the user, represented by the following keys:
    level (int)
    password (str)
    sshkeys (list)
The level is an integer between 0 and 15, where 0 is the lowest access and 15 represents full access to the device.'''
