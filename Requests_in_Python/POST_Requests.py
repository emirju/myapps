###    HTTP POST requests in Python   ###

import requests

url = 'https://enhktdry5i2hc.x.pipedream.net'  # check here : https://requestbin.com/r/enhktdry5i2hc/1p1FnFa3mrtdnx5UpwwPwGo1RTG

r = requests.post(url)

#-------------------------------------------------------------------

payload = {  # here in PAYLOAD is a JSON object with NAME and AGE
    "name": "emir",
    'age' : "29"
    }
r = requests.post('https://reqres.in/api/users', json=payload) # sending a POST request to CREATE, request will be convertet to a JSON object

print(r) # response status code will be 201(this means something was created succsessfully )
print(r.text)