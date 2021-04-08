
from netmiko import Netmiko
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

try:
    connection = Netmiko(host='192.168.128.100', port='22', username='emir', password='cisco', device_type='cisco_ios')
    print("   *** Connection to a device ***    " )
except NetmikoTimeoutException:
    print(" * This Device is not reachable * ")

except AuthenticationException:
    print('  *** Authentication failure ***   ')

except SSHException:
    print("  * Make sure SSH is enabled in device *  ")

sh = connection.send_command('sh version')
print(sh)


print('Closing connection')
connection.disconnect()

'''when the IP is wrong this is the output : netmiko.ssh_exception.NetmikoTimeoutException'''
'''when authentication is wrong this is output : paramiko.ssh_exception.AuthenticationException: Authentication failed'''
