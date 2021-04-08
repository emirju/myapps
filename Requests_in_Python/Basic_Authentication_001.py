
import requests
from requests.auth import HTTPBasicAuth

username = input("Enter username : ")
password = input("Enter password : ")

url = 'https://httpbin.org/basic-auth/emir/secret'  # the username should be emir; the password should be secret if we want to authenticate

r = requests.get(url, auth=HTTPBasicAuth(username, password))
print(r)
