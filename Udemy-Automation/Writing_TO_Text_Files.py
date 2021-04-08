
with open("myfile.txt", 'w') as file:
    file.write("First line to be added on text document \n") # \n will add next line to be as NEW line
    file.write("Second line to be added on text document\n")
### go run the script so new 'myfile.txt' will be added, it will have a text "First line to be added on text document "
### using w - write file will be created if it doesnt exist, but if it exist it will be overwriten

with open('myfile.txt', 'a') as file:
    file.write("Third line to be added on text document\n")
## a - append, it will add new line on next new free line
## with a-append Python creates a file if it doesnt exist or append new line if it exist


file = open("myfile.txt", 'r+')
file.write('Line added with r+ \n')
doc = file.read()
print(doc)
### ' r+ ' this access mode is used for both reading and writing on file
### By this, line will be added ad beging of the file(first row), not at the end

file.close()



