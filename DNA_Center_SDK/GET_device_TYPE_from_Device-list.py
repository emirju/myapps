from dnacentersdk import api

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser',
                       password='Cisco123!')

devices = dna.devices.get_device_list()
for device in devices.response:
    print("Device Type : " + device.type)