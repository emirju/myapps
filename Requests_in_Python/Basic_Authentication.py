import requests
from requests.auth import HTTPBasicAuth ## This allowes me to pass username and pass using HTTP BasicAuth


r = requests.get('https://httpbin.org/basic-auth/emir/secret', auth=HTTPBasicAuth('emir','password'))
# using AUTH parameter and taking BasicAuth that has been imported and inside pass the username and pass
print(r)
### after issuing this result will be : <Response [401]>  (there is correct username : emir but secret and password are not the same)

r = requests.get('https://httpbin.org/basic-auth/emir/secret', auth=HTTPBasicAuth('emir','secret'))
print(r) # the result is <Response [200]>   response code means everything is OKEY

