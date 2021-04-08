
from ncclient import manager

csr1000v = manager.connect(
            host='ios-xe-mgmt.cisco.com',
            port=10000,
            username='developer',
            password='C1sco12345',
            hostkey_verify=False,
            device_params={'name':'csr'}
)

schema = csr1000v.get_schema("ietf-interfaces") ## Get schema (TREE) for this ietf-interface Capabilities
print(schema)



