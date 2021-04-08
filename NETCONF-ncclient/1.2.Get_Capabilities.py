
from ncclient import manager

router = {
    'host':'ios-xe-mgmt.cisco.com',
    'port':10000,
    'username':'developer',
    'password':'C1sco12345',
    'hostkey_verify':False,
    'device_params':{'name':'csr'}
}

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'],
                     hostkey_verify=router['hostkey_verify'], device_params=router['device_params']) as m:
    for capabilities in m.server_capabilities:
        print('*' * 100)
        print(capabilities)
        