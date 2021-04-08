
text = open("Text_File.txt")
output = text.read(11)  #It will read and print it out just first 11 Characters
print(output)

output = text.read(2)
print(output)

print(text.tell()) # Result of TELL will be 13 (=11+2) cursor is at position  13

# To move to a specific position inside the file, we use another method called SEAK
text.seek(7) # cursor will go at position 7 and first Character will be "o"
print(text.read(4)) # Reading 4 Characters

text.close() # Close the file by calling the close method 