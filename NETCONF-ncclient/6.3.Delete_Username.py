from ncclient import manager
csr1000v = manager.connect(host='ios-xe-mgmt.cisco.com',
                           port=10000,
                           username='developer',
                           password='C1sco12345',
                           hostkey_verify=False,
                           device_params={'name':'csr'}
)
user_conf = """
<config>
    <native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username operation='delete'>
			<name>netconf_test</name>
			<privilege>15</privilege>
			<secret>
				<encryption>0</encryption>
				<secret>netconf_password</secret>
			</secret>
		</username>
	</native>
</config>
"""
result = csr1000v.edit_config(user_conf, target='running')
print(result)