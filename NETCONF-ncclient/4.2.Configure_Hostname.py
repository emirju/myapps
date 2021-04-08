from ncclient import manager
csr1000v = manager.connect(host='ios-xe-mgmt.cisco.com',
                           port=10000,
                           username='developer',
                           password='C1sco12345',
                           hostkey_verify=False,
                           device_params={'name':'csr'}
)
CONFIGURATION = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>csr1000v</hostname>
    </native>
</config>
"""
edit_conf = csr1000v.edit_config(CONFIGURATION, target='running')  # TARGET configuration is running config and aslo variable CONFIGURATION
print(edit_conf)