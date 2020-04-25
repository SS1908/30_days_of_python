"""
    Python Classes/Objects

    Python is an object oriented programming language.
    Almost everything in Python is an object, with its properties and methods.
    A Class is like an object constructor, or a "blueprint" for creating objects.

"""
#to create a class,use keyword 'class'

class computer:

    def config(self):
        print("cpu = i7","ram = 16gb","storage = 1TB")

 #if you are use class name for calling a method,you need to pass an object of that class
c1 = computer()
computer.config(c1)

#if you are using a object name for aclling a method .then you not need to pass an object parameter
c2 = computer()
c2.config()

