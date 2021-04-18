#importing MerakiSDK Client, this client is what sets up our whole connection
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from pprint import pprint

token = "deeb656da181f4f3c63adbde7ff2b64ae8e558d4" # token generated in portal https://n201.meraki.com/o/Ugi9qb/manage/users/edit?only_path=false&protocol=https
meraki = MerakiSdkClient(token) # set variable meraki and this is equal the Connection OBJECT (connecting into MERAKI)
         # after = specify MerakiSdkClient and use token inside prentesise, this will handle all authentication, storing token for all requests

orgs = meraki.organizations.get_organizations() # Store list of ORGANIZATIONS in variable called "orgs"

pprint(orgs)
