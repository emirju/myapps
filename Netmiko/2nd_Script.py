
### Instead of using Netmiko Class we will use ConnectHandler and DICTIONARY with it
from netmiko import ConnectHandler
###Creating a DICTIONARY for ConnectHandler which containes information for device
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.128.129',
    'username': 'emir',
    'password': 'cisco',
    'port': 22,
    'secret':'automation'

}
    ##Creating an object called conn
conn = ConnectHandler(**cisco_device) #** this is a kwargs style of calling functions, it unpacks a DICTIONARY into the FUNCTION ARGUMENTs
print("  *** Connecting to a device ***  ")
    ### PROMPT -  we can find it in which prompt we are
prompt = conn.find_prompt()
print(prompt)
     # calling the enable method of the CONN OBJECT
conn.enable()  # need to pass enable secret : ValueError: Failed to enter enable mode. Please ensure you pass the 'secret' argument to ConnectHandler.

prompt = conn.find_prompt()
print(prompt)
    ## Sending command to the device :
#variable_output = conn.send_command('show run')
#print(variable_output)

'''Global configuration mode'''
print(conn.check_config_mode())   ###Checking if we are already in global conf mode, it returns FALSE it means we are not in global mode
conf_mode = conn.config_mode() ###entering global configuration mode, we call config mode method of CONN object
print(conf_mode)

'''we can use also 
if not conn.check_config_mode()
       conn.config_mode() '''

    #Closing connection
print(' *** Connection is diconnected *** ')
conn.disconnect()
