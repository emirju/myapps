import napalm

ip_address = input("Enter the IP Address of device : ")
username = input("Enter your username : ")
password = input("Enter your password : ")
enable = {'secret': 'automation'}

driver = napalm.get_network_driver('ios')
device = driver(ip_address, username, password,timeout=60, optional_args=enable) # timeout – (int) Time in seconds to wait for the device to respond

device.open()

output = device.get_environment()
print(output)

device.close()
'''
get_environment()
Returns a dictionary where:
    **fans is a dictionary of dictionaries where the key is the location and the values:
        status (True/False) - True if it’s ok, false if it’s broken
    **temperature is a dict of dictionaries where the key is the location and the values:
        temperature (float) - Temperature in celsius the sensor is reporting.
        is_alert (True/False) - True if the temperature is above the alert threshold
        is_critical (True/False) - True if the temp is above the critical threshold
    **power is a dictionary of dictionaries where the key is the PSU id and the values:
        status (True/False) - True if it’s ok, false if it’s broken
        capacity (float) - Capacity in W that the power supply can support
        output (float) - Watts drawn by the system
    **cpu is a dictionary of dictionaries where the key is the ID and the values
        %usage
    **memory is a dictionary with:
        available_ram (int) - Total amount of RAM installed in the device
        used_ram (int) - RAM in use in the device'''