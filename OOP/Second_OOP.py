######      _init_  Method in Python        ######

class Computer:

    ###We can use special Method which is Variable in a CLASS (special method __init__)
    def __init__(self):  ## We use __init__ to INITALIZE Variables
        print(' *** In __init__ ***')

object1=Computer() # Creating OBJECT
print(object1)
print(type(object1))

'''If we want to work with config like in First_OOP we have to CALL config because it will be not
 executed. Idea behind INIT is will be called automatically
'''