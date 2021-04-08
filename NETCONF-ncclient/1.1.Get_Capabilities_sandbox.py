# Geting all CAPABILITIES from the Router (for SANDBOX Lab) https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology

from ncclient import manager

csr1000v = manager.connect(
            host='ios-xe-mgmt.cisco.com',
            port=10000,
            username='developer',
            password='C1sco12345',
            hostkey_verify=False,
            device_params={'name':'csr'}
)

for single_capabilitie in csr1000v.server_capabilities:   # by server_capabilities we are gettin SERVER NETCONF CAPABILITES
    print(single_capabilitie)

csr1000v.close_session()
