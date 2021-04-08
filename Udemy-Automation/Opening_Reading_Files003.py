

with open('Text_File.txt', 'r') as file:
    print(file.read())

print(file.closed)  # notice that it READ and PRINT out the entire content of the file and it also AUTOMATICALLY CLOSE it