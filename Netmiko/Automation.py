from netmiko import ConnectHandler
cisco_device = {
    'device_type':'cisco_ios',
    'host':'192.168.128.129',
    'username':'emir',
    'password':'cisco',
    'secret':'automation',
    'port': 22
}
connect = ConnectHandler(**cisco_device)

users_output = connect.send_command('sh users')
print('#' *70, '\n', users_output,'#'*70)

print(' *** Entering Enable Mode *** ')
connect.enable()
    ### Creating a LIST called commands
commands = ['hostname R-001', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'do write memory']
    ### Having the LIST with commands need to CALL SEND CONFIG SET METHOD of CONNECT OBJECT
commands_output = connect.send_config_set(commands,cmd_verify=False) ## it takes a commands list as its ARGUMENT
print(commands_output)

connect.enable()
## Netmiko offers us a method called SEND_CONFIG_FROM_FILE and it send all from that file into SSH connection
print(' ... Sending commands from file ospf.txt ...')
output_var = connect.send_config_from_file('ospf.txt ')   ## the ARGUMENT will be file ospf.txt
print(output_var)

print(" *** Closing connection *** ")
connect.disconnect()
