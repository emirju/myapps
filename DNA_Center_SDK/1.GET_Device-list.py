from dnacentersdk import api
import json

dna =  api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                        username='devnetuser',
                        password='Cisco123!')

############### DEVICES #############
        # Print Device Details

devices = dna.devices.get_device_list()
print(json.dumps(devices, indent = 5))


