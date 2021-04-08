from netmiko import ConnectHandler
user = input("Enter your username : ")
password = input("Enter your password : ")
device_info = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.128.129',
    'username' : user,
    'password' : password,
    'secret' : 'automation'
}
connect = ConnectHandler(**device_info)

interface = input("Enter the interface : ")
int_output = connect.send_command('show ip int ' + interface)

if 'Invalid input detected at' in int_output:
    print("You entered invalid interface ")
    while 'Invalid input detected at' in int_output:
        ## If invalid interface entered try again
        print(" ** Enter your interface again ** ")
        interface = input("Enter the interface : ")
        int_output = connect.send_command('show ip int ' + interface)
        print(f'  # show ip int ' + interface)
        first_list = int_output.splitlines()[0]
        print(first_list)
        ### Enabling the interface if it is SHUT DOWN
        if not 'up' in first_list:
            print("  ***  This interface is DOWN  *** \n  ### Enabling the interface ### \n")
            connect.enable()
            config_send = ['interface ' + interface, 'no shut', 'exit']
            send_config = connect.send_config_set(config_send)
            print(send_config)
        else:
            print("  ***  Interface is already UP  ***  ")
else:
    print(f'  # show ip int ' + interface )
    first_list = int_output.splitlines()[0]
    print(first_list)
    ### Enabling the interface if it is SHUT DOWN
    if not 'up' in first_list:
        print("  ***  This interface is DOWN  *** \n  ### Enabling the interface ### \n")
        connect.enable()
        config_send = ['interface ' + interface , 'no shut', 'exit']
        send_config = connect.send_config_set(config_send)
        print(send_config)
    else:
        print("  ***  Interface is already UP  ***  ")

connect.disconnect()