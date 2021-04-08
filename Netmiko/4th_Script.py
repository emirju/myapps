
from netmiko import ConnectHandler
device_informations = {
    'device_type':'cisco_ios',
    'host':'192.168.128.129',
    'username':'emir',
    'password':'cisco',
    'secret':'automation',
    'port':22
}
connect = ConnectHandler(**device_informations)

print(' *** Entering Enable Mode *** ')
connect.enable()
### After config_commands = commands are writen as a STRING usign a unik separator ( ; )
config_commands ='username netmiko secret netmiko ; hostname R-1 ;exit ;sh run | s username'
## Calling send config set method
output = connect.send_config_set(config_commands.split(';')) ## this will transform upper STRING into a LIST, it will return a LIST
print(output)

wr = connect.send_command('write')
print(wr)

print(" *** Closing connection *** ")
connect.disconnect()

