## Geting all CAPABILITIES from the Router (for GNS3 Lab)

from ncclient import manager  # ncclient is python library we use for interacting with networking devices using NETCONF protocol
                              # manager is the module of ncclient for interacting with DEVICE
router = manager.connect(
            host='192.168.128.131',
            port=22,           # I can't get scripts to work when using the default NETCONF port 830 or 10000. The script always fails and ...
            username='emir',   # I have to add SSH port 22 in the script for it to work
            password='cisco',
            hostkey_verify=False,
            device_params={'name':'csr'}
)

for csr1000v_Capabilities in router.server_capabilities:   # by server_capabilities we are gettin SERVER NETCONF CAPABILITES
    print(csr1000v_Capabilities)

router.close_session()

'''Supported device handlers =
  Cisco:
        CSR: device_params={‘name’:’csr’}
        Nexus: device_params={‘name’:’nexus’}
        IOS XR: device_params={‘name’:’iosxr’}
        IOS XE: device_params={‘name’:’iosxe’}  '''

