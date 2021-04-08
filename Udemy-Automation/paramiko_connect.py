import paramiko

# creating an ssh client object
ssh_client = paramiko.SSHClient()
#print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 10.0.0.1')
ssh_client.connect(hostname='192.168.128.129', port='22', username='emir', password='cisco',
                   look_for_keys=False, allow_agent=False)



# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
# ...

print('Closing connection')
ssh_client.close()