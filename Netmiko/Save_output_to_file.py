# Import program dependencies

from netmiko import ConnectHandler
import getpass

# Read from a list of hostnames to connect to
hosts = open('hosts.txt', 'r')
hosts = hosts.read()
hosts = hosts.strip().splitlines()

# Get UserName and password from input
userName = input('Username: ')
passWord = getpass.getpass()

# Loop to process hosts in hosts.txt file
for host in hosts:
    # Define device type and connection attributes
    Brocade_ICX = {
        'device_type': 'brocade_fastiron',
        'ip': host,
        'username': userName,
        'password': passWord),
    }

# Netmiko SSH Connection Handler
net_connect = ConnectHandler(**Brocade_ICX)

    # open file to write command output
    file = open(host + '_output.txt', 'w')

    # Execute commands
    output = net_connect.send_command('skip-page-display')
    output = net_connect.send_command('show run')

    # Print output to console screen
    print('-------------- Output from ' + host + '------------------')
    print(output)
    print()
    print()

    # Write output to file above
    file.write(output)
    file.close()