import requests

# r = requests.get('https://enhktdry5i2hc.x.pipedream.net?key1=value1&key2=value2')
    # Sending to this URL two parameters, anything after ? does not change the URL but just sending some date with it

payload = {'name' : 'emir', 'age' : '29'}
r = requests.get('https://enhktdry5i2hc.x.pipedream.net', params=payload )

#--------------------------------------------------------------------------------
                  # Custom HEADER #
# Passing a TOKEN that is used for authentication in a HEADER

header = {'my-token' : 'gr34tfdgeasrgrewg343t651465tgregdf'}
r = requests.get('https://enhktdry5i2hc.x.pipedream.net', headers=header)
# headers = parameter  ; header = dictionary 