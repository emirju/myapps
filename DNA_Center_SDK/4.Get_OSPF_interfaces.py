from dnacentersdk import api
import json

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser',
                       password='Cisco123!')

devices = dna.devices.get_ospf_interfaces()
print(json.dumps(devices,indent = 4 ))



