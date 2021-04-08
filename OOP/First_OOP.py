#####       CLASS and OBJECT in Python        ######
class Computer:   # defining a CLASS using CLASS keyword and this CLASS will have a name Computer
    '''We can put here two things after defining the CLASS :
        1. Attributes --> Variables
        2. Behaviour  --> Methods (Functions)
    '''
    def config(self):   ## Defining the METHOD which is called #config#
        print("i7, 16GB, 1TB")
'''-----------------------------------------------------------------------------------------------'''
com1=Computer()  #Creating OBJECT
### com1 is the OBJECT of CLASS Computer, now we have CLASS and we have OBJECT, we need to call the config

com1.config()  ##First option how we can call the config(method or function). One CLASS can have multiple OBJECTs
print(type(com1))
'''-----------------------------------------------------------------------------------------------'''

Computer.config(com1) ## Second option how we can config, here we pas com1 as argument

'''-----------------------------------------------------------------------------------------------'''
a=8
print(type(a))
b='i7'
print(type(b))
'''-----------------------------------------------------------------------------------------------'''

