"""
    we have a two type of variable in class :-  1) instance variable
                                                2)class variable

    instance variable is changes object to object.
    class variable is same for all the instance/object of the class.

"""
class car:

    #this is a class variable
    #class variable define outside the __init__ method.
    wheels = 4

    #this is a instance variable
    def __init__(self):
        self.comp = "BMW"
        self.mile = 10

c1 = car()
c2 = car()

# you can access class variable using object_name or class_name.
print(c1.comp,c1.mile,c1.wheels)
print(c2.comp,c2.mile,car.wheels)
print()

#you can change the value of an instance variable.
c1.mile = 8

#we can also change the value of class variable.
car.wheels = 5

print("After changing value of instance and class variable")
print(c1.comp,c1.mile,car.wheels)
print(c2.comp,c2.mile,c2.wheels)