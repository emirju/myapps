from ncclient import manager
DEVICE = manager.connect(host='ios-xe-mgmt.cisco.com',
                           port=10000,
                           username='developer',
                           password='C1sco12345',
                           hostkey_verify=False,
                           device_params={'name':'csr'}
)
config = DEVICE.get_config('running')

save_to_file = open('running.xml', 'w')
save_to_file.write(str(config))
save_to_file.close()