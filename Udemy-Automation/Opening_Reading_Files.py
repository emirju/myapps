
###      Opening and reading files    ###

# In order to Read or Write files, you don't need to import any module, it is handled natively in language
### Use OPEN function to get the file object(File Objects contain, METHODS and ATRIBUTES) that can be used
### to collect information about the file you opened ###

#    Create File OBJECT simply called f   !!!

f = open("Text_File.txt", "r") # First argument is File name (Text_File.txt)
                               # Second argument is optional is called access mode or simply mode
                               # and idicates how file will be opened,
                               # The most used modes are :
                               #  1. r - Read ; 2. w - Write ; 3. a = Append
                               # if mode is not specified it will be opened in Read Only mode ( DEFAULT )
### In Python file is categorized as TEXT or BINARY (DEFAULT is TEXT file)

#Having the file opened that see how to access and print out data in the text_file
#First method is READ, it READs and RETERNS entire content of the file as the STRING
content = f.read()
print(content)

#When we are done with the file, we must CLOSE it
#There is an atribute of file object called CLOSED that is TRUE if the file is CLOSED
print(f.closed)
f.close() # now file will be closed 
print(f.closed)