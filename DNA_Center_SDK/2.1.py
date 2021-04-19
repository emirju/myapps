from dnacentersdk import api

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com',
                       username='devnetuser',
                       password='Cisco123!')

print('{0:25}{1:3}{2:45s}{3:3}{4:15s}'.format("Device Name", "|", \
"Device Type", "|", "Up Time"))
print('-' * 95)

devices = dna.devices.get_device_list()
for device in devices.response:
    print('{0:25s}{1:3}{2:46s}{3:3}{4:15s}'.format(device.hostname, \
    "|", device.type, "|", device.upTime))
    print('-'*95)