### Connecting to a networking device
#   First we must import the GET NETWORK DRIVER from NAPALM library
from napalm import  get_network_driver

#  Second create the driver OBJECT
driver = get_network_driver('ios') # in brackets we must specify the driver and it represents type of device NAPALM is connecting to...THIS IS CISCO IOS

# Now creating another OBJECT where :
# 1st ARGUMENT is IP ADDRESS; 2nd ARGUMENT is USERNAME ; 3rd ARGUMENT is PASSWORD; 4th ARGUMENT IS ENABLE password
optional_arguments = {'secret': 'automation'}#creating a VARIABLE and it is of type dictionary where KEY is SECRET and value is our enable password 'automation'
ios = driver('192.168.128.129', 'emir', 'cisco', optional_args= optional_arguments)

## Now ios object is created we are going to open it
ios.open() ## By all of this communication is opened so we can communicate to our device

### Here in between open and close will be our NAPALM code, so that PRINT ALL methods that it offers
print(dir(ios))

# After finishing it is necessary to close
ios.close()

