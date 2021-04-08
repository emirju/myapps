
from netmiko import ConnectHandler
device_information = {
    'device_type': 'cisco_ios',
    'host': '192.168.128.100',
    'username': input("Enter your username : "),
    'password': input("Enter your password : "),
    'secret': 'automation',
    'port': '22'
}
connect = ConnectHandler(**device_information)

sh_vlan = connect.send_command('show vlan brief')
print(sh_vlan, '#'*80)

connect.enable()

for n in range(10, 50, 10):
    print(" *** Creating VLAN : " + str(n))
    config_vlans = ['Vlan ' + str(n), 'name Emir ' + str(n)]
    send_commands = connect.send_config_set(config_vlans, cmd_verify=False)
    print(send_commands)


connect.disconnect()