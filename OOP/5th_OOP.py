            ####     Types of Methods    ####

''' Objects will have two things " : 
        1. Variables - to store Data
        2. Methods - for the behaviour, if we want to perform some operations '''

'''There are 3 types of METHODS : 
    1. Instance methods (two types : 1. Accessor Methods &&& 2. Mutator Methods )
    2. Class methods
    3. Static methods
    '''

class Student:

    school = ' UP ' ### CLASS VARIABLE

    def __init__(self, mark_1, mark_2, mark_3 ):       #Function
        self.m1 = mark_1  # Defining 3 variables
        self.m2 = mark_2  # instead of mark_2 we can pass our own values, but values will be passed when we create an object
        self.m3 = mark_3
        ### m1, m2 and m3 are INSTANCE VARIABLES

    def avg(self): ### This is the INSTANCE METHOD, because we are passing SELF, self belongs to a particular object
        return (self.m1 + self.m2 + self.m3 )/3

    ### CLASS METHODs, now we will work will CLASS VARIABLE (school = ' UP ')
    def info(cls): # We dont wont to work with self but we will work with CLASS(cls)
        return cls.school

# Creating OBJECTs
s1 = Student(9,10,8)  # now passing values to these two objects
s2 = Student(7,10,9)

### Call the avg method for object s1 (student 1) for INSTANCE METHOD
print(s1.avg())

## Calling info for CLASS METHODs
print(s1.info())