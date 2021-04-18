from dnacentersdk import api
import json

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser',
                       password='Cisco123!')

device_ip_address = dna.devices.get_network_device_by_ip(ip_address="10.10.22.66") #Returns the network device by specified IP address
print(json.dumps(device_ip_address, indent=4))