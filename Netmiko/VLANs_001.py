from netmiko import ConnectHandler
device_information = {
    'device_type': 'cisco_ios',
    'host': '192.168.128.100',
    'username': input("Enter your username : "),
    'password': input("Enter your password : "),
    'secret': 'automation',
    'port': '22'
}
print('\n   *   *   *    Connecting to a deivce   *   *   *   \n')
connect = ConnectHandler(**device_information)
connect.enable()

# Creating a list of all Vlan's
vlan_names = ['Management', 'Staff', 'Guest', 'HR-Office', 'Administation', 'Finance']

a =10
while a <= 60:

    for i in vlan_names:
        print("         *** Creating Vlan " + str(a) + " ***  ")
        vlan_num = ['Vlan ' + str(a), 'name ' + str(i)]
        a += 10
        send_conf = connect.send_config_set(vlan_num,cmd_verify=False)
        if vlan_names == 'Finance':
            break
        print(send_conf)

print("\n  ##### Saving the configuration #####   ")
save = connect.save_config()
print(save)

print("#"*80, "\n   *** show vlan brief ***    ")
sh_vlan=connect.send_command('show vlan brief')
print(sh_vlan)

print("\n   *   *   *    Closing connection   *   *   *   ")
connect.disconnect()
