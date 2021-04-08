
weight = int(input("Put your weight : "))
unit = input("Weight in Lbs or Kg : ")

if unit.upper() == "L":
    result = weight * 0.45
    print( f'You are {result} kilos')
elif unit.upper() == "K":
    result = weight // 0.45
    print(f"You are {result} pounds")
else:
    print("Mistake")
