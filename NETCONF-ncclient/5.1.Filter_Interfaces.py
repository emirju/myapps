#### this is openconfig.net/yang/interfaces (openconfig Data Model)
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
<interfaces xmlns="http://openconfig.net/yang/interfaces">
	<interface>
		<config>
			<name></name>
			<description></description>
			<enabled></enabled>
		</config>
		<subinterfaces>
			<subinterface>
				<ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
					<addresses>
						<address>
							<ip></ip>
							<config>
								<ip></ip>
								<prefix-length></prefix-length>
							</config>
						</address>
					</addresses>
				</ipv4>
			</subinterface>
		</subinterfaces>
	</interface>
</interfaces>
</filter>
"""


print(csr1000v.get_config('running', FILTER))
