from ncclient import manager
csr1000v = manager.connect(host='ios-xe-mgmt.cisco.com',
                           port=10000,
                           username='developer',
                           password='C1sco12345',
                           hostkey_verify=False,
                           device_params={'name':'csr'}
)
FILTER = """
<filter>
		<native
			xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
			<hostname></hostname>
		</native>
</filter>
"""
hostname_filter = csr1000v.get_config('running', FILTER)
print(hostname_filter)