

try:
    number = int (input("Enter Value : "))
    print(number)
    value=10/0

except ValueError:
    print("Invalid input")


except ZeroDivisionError:
    print("Value divided by zero")