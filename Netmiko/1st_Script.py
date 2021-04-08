### Importing just class called Netmiko, not entire netmiko library (import netmiko)
from netmiko import Netmiko ###Netmiko Class

''' Creating a connect object by calling class constructor (Netmiko)
    inside Netmiko we will create an ARGUMENTS '''
connection = Netmiko(host='192.168.128.129', port='22', username='emir', password='cisco', device_type='cisco_ios')
## Last argument device_type= is supported platform and it is cisco_ios as it is cisco router
###Up to hear we have create a script to connect successfully on cisco router through SSH port 22
### password argument on device is username emir secret 5 cisco; on script use password not secret

''' after successfully connected to router we can SEND COMMANDS through this connection 
    to do this we will use send command method of CONNECT object'''
output = connection.send_command('sh ip int brief') ##Saving output on variable called output
print(output)

print('##############################################################################')

output1 = connection.send_command('show users')
print(output1)

###diconecting from device
print('Closing connection')
connection.disconnect()

#compering to Paramiko, we didnt need to execute term len0 with Netmiko to display entire output of show command, it is by default on Netmiko