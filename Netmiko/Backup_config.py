from netmiko import ConnectHandler

# getting the current date (year-month-day)
from datetime import datetime ## First datetime is the Module and second one is there is a Class called datetime
now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minutes = now.minute

IP = input("Enter the IP address of device : ")
user = input("Enter your username : ")

device_info = {
        'device_type' : 'cisco_ios',
        'ip' : IP,
        'username' : user,
        'password' : input("Enter your password : "),
        'secret' : 'automation',
        'port' : 22
    }
conection = ConnectHandler(**device_info)

print("  \n ***  Connection to a device : " + IP.strip() + ' ***  ')
connection = ConnectHandler(**device_info)

show_output = connection.send_command('show ip int brief')

#Creating the hostname for backup file (#hostname #date #backup .txt )
prompt = connection.find_prompt()
hostname = prompt [0 : -1] ## if we print PROMPT will get hostname with (#) at the end; ex.(Router#)so by [0:-1] last char which is # will not be taken

#Creating a FILE(filename) with complete name for backup configs, there will be hostname dates and some text at the end
filename = f'{hostname}_{day}_{month}_{year}_backup_logs.txt'

#Writing the backup config to the filename FILE
with open(filename,'w')as backup:  ### filename is variable here and it is not in ( ' ' ) it is variable that already contains the string.. UP UP UP
    backup.write(f'____Backup for hostname {hostname} and IP address : {IP}____\n ')
    backup.write('#'*100 + '\n')
    backup.write(show_output)

print('*** Closing connection ***')
conection.disconnect()
