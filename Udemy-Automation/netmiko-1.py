from netmiko import Netmiko
connection = Netmiko(host='192.168.128.129', port='22', username='emir', password='cisco', device_type='cisco_ios')


# sending a command and getting the output
output = connection.send_command('sh ip int brief')
output1 = connection.send_command('sh users')

print(output)
print("##################################################")
print(output1)



# closing the connection
print('Closing connection')
connection.disconnect()