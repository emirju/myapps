
### Configuring a Networking Device from a File

from netmiko import Netmiko
connection_object = Netmiko (device_type='cisco_ios',host='192.168.128.129', port=22, username='emir', password = 'cisco', secret='automation')

print(' \n   *** Entering Enable Mode *** \n')
connection_object.enable()

## Netmiko offers us a method called SEND_CONFIG_FROM_FILE and it send all from that file into SSH connection
print(' ... Sending commands from file ospf.txt ...\n')
output_var = connection_object.send_config_from_file('ospf.txt ')   ## the ARGUMENT will be file ospf.txt
print(output_var)

print(' \n     *** Closing the connection *** ')
connection_object.disconnect()
