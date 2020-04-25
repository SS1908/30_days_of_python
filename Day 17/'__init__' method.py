"""
    To understand the meaning of classes we have to understand the built-in __init__() function.

    All classes have a function called __init__(), which is always executed when the class is being initiated.

    Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

"""

class computer:

    #The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("configration is ",self.cpu,self.ram)


cpu_input = input("enter a cpu ")
ram_input = input("enter a ram ")

c1 = computer(cpu_input,ram_input)
c1.config()
