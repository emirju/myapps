
names = ["Emir", "Admir", "Amina"]
print(names)
print(names [1])
print(names[:])

#-----------------------------#
numbers = [3,10,5,9,555]
copy_of_numbers = numbers.copy()  # this copies original list
numbers.append(25)
numbers.insert(0,99)  # 0 index position is 0 ;;; second value is object on this list, it is number 99
numbers.remove(3)
print(numbers)
print(copy_of_numbers)
max = numbers[0]   #start from first number
for num in numbers:
    if num > max :
        max=num
print(max)