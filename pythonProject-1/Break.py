

x=int(input("How much do you want : "))
i=1

max=5
while i<=x:
    if i>max:
        print("There are just 5 Laptops left, you cant have", x ,"Laptops")
        break #This means just jump out of the LOOP when the max number is achieved
    print(i, "Laptop")
    i+=1

