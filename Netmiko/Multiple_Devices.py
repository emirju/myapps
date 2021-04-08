from netmiko import ConnectHandler

IPs_List = open('Device-IP-List') ### open a Device-IP-List where are IP information for all devices

user = input("Enter your username : ")

for IP in IPs_List:   ### use LOOP FOR which will use one by one all IPs from .txt
    device_info = {
        'device_type' : 'cisco_ios',
        'ip' : IP,
        'username' : user,
        'password' : input("Enter your password : "),
        'secret' : 'automation',
        'port' : 22
    }
    print("  \n ***  Connection to a device : " + IP.strip() + ' ***  ')
    connection = ConnectHandler(**device_info)

    sh=connection.send_command('sh ip int brief')
    print(sh)

    connection.disconnect()