###Comparation condition

password = input("Enter your password here : ")
print(len(password))

if len(password) < 5:
    print("Password must have at least 5 characters")
elif len(password)>15:
    print("Password can have maximum 15 characters")
else:
    print("Password looks good")
