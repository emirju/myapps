
class Computer:
    def __init__(self, cpu, ram):  ## There are two parametars-arguments (cpu, ram), self would be an object
        self.cpu1=cpu ## Every object need to have a value(parameters-arguments)
        self.ram1=ram ## By this value cpu will be part of object self

    def print_this(self):
        print("Print values are : ", self.cpu1, self.ram1)

## There are two object, and each object will have its own variable(it own cpu and it own ram)
comp1 = Computer("i5", 8)  ##i5 goes to cpu as argument, and cpu is assigned to object self,and 8 goes to ram
comp2 = Computer("Ryzen 3 ",16 )

## Two options of printing
print(comp1.cpu1, comp1.ram1)
comp1.print_this()

