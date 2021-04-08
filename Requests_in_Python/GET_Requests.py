### HTTP GET requests in Python  ###
import requests #Begin by importing the Requests module
import json
#---------------------------------------------------------------
'''url = "https://reqres.in/api/users/2"
list = requests.get(url)
print(json.dumps(list.json(), indent=2))'''
#  To retrieve information (resources) from an API, you typically use an HTTP GET request #
#---------------------------------------------------------------

response_variable = requests.get('https://enhktdry5i2hc.x.pipedream.net')  # requests is a  library
# requests will be sent to a URL above; check it here : https://requestbin.com/r/enhktdry5i2hc
#---------------------------------------------------------------

r = requests.get('https://reqres.in/api/users/2')
print(r)
print(r.text)
