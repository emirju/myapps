## this is yang:ietf-interfaces (ietf Data Model)
from ncclient import manager
router = manager.connect(host="ios-xe-mgmt.cisco.com",
                         port=10000,
                         username="developer",
                         password="C1sco12345",
                         hostkey_verify=False,
                         device_params={'name': 'csr'}
)
CONFIGURATION = """
<config>	
    <interfaces
		xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>GigabitEthernet3</name>
			<description>WAN INTERFACE</description>
			<type
				xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd
			</type>
			<enabled>true</enabled>
			<ipv4
				xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>192.168.1.5</ip>
					<netmask>255.255.255.0</netmask>
				</address>
			</ipv4>
		</interface>
	</interfaces>
</config>"""
edit_configuration = router.edit_config(CONFIGURATION, target='running')
print(edit_configuration)