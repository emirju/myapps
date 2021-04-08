'''Creating a list of commands and using FOR loop to execute commands
  First script IMPORTs NETMIKO and them using DICTIONARY that represent the device and down the ConnectHandler method
  authenticates to a device and returns the connection to the OBJECT called connection
  After successfull authenticating is to enter ENABLE mode by calling ENABLE METHOD without any argument
  Then we will create a list with all commands '''
from netmiko import ConnectHandler
cisco_device = {
    'device_type':'cisco_ios',
    'host':'192.168.128.129',
    'username':input("Enter your username : "),
    'password':input("Enter your password : "),
    'port':22,  # Optional
    'secret':'automation'
    }
connection = ConnectHandler(**cisco_device)

print(' *** Entering enable mode *** ')
connection.enable()
    ### Creating a LIST called commands
commands = ['hostname R-001', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'do write memory']

    ### Having the LIST with commands need to CALL SEND CONFIG SET METHOD of CONNECTION OBJECT
output = connection.send_config_set(commands,cmd_verify=False) ## it takes a commands list as its ARGUMENT
print(output)                                 ## This method will enter automatically GLOBAL conf mode before making configuration changes and exit it at the end when it finish.
print(' *** Current mode : ', connection.find_prompt())

users = connection.send_command('show users')
print('#' *62, '\n' ,users)

print(" *** Closing connection *** ")
connection.disconnect()