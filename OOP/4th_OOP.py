                              ### Types of Variables ###

''' There are two types of Variables :
      1. Instance Variable
      2. Class (Static) Variables  '''

class Computer :
    '''If we want to create a Variable which is common for all Objects, in this case need to def variable outside of __init__ but inside class
        by this variable becomes CLASS (STATIC) VARIABLE  '''
    SDD = "1Tb"

    def __init__(self):
        self.cpu = 'i7'
        self.ram = '8GB' # there are two INSTANCE VARIABLES cpu = i7 and ram = 8GB, and we can change it down, these are two default values

object_1 = Computer() # We have one object here
object_2 = Computer() # Second object

object_1.ram = '16GB' # Value of ram has change now from 8 to 16 for object_1

print(object_1.cpu, object_1.ram)
print(object_2.cpu , object_2.ram)

print(object_1.cpu, object_1.ram, object_1.SDD) ## adding STATIC variable, SDD is common to all objects

##  If we want to change or modify the SDD we have to use CLASS name
Computer.SDD = '500 GB' ## This change will affect all objects
print("Value of SDD is : " + object_1.SDD)
