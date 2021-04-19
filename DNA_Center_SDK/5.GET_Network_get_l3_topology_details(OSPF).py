from dnacentersdk import api
import json

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser',
                       password='Cisco123!',
                       version='1.2.10')

device = dna.networks.get_l3_topology_details(topology_type='OSPF')
print(json.dumps(device, indent=4))


