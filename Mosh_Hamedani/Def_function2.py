
## Keyword ARGUMENTS ##

def user_input(first_name, last_name):
    print("*********************************")
    print(f"     Hello {first_name} {last_name} ! ")


print("Please provide you informations ")
print("********************************* ")
##user_input("Emir", "Jukovic")  # Here are two keyword ARGUMENTS first_name and last_name
data = user_input(first_name = input("Enter your name : "), last_name=input("Enter your last name : "))
