

i=1
while i<=10:
    print("Multiplication by : ", i)

    j=1
    while j<=10:
        print(i, '*', j, ' = ', i*j, end=" ||| ")
        j+=1
    i=i+1
    print()