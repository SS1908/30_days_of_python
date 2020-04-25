#you can modify the properties of object

class student:

    def __init__(sillybobject,name,age):
        sillybobject.name = name
        sillybobject.age = age

    def info(self):
        print(self.name,end=" ")
        print(self.age)

s1 = student("sagar",21)
s2 = student("nayan",20)

print("before modifing value")
s1.info()
s2.info()
print()

s1.age = 10
s2.name = "meet"
print("after modifing value")
s1.info()
s2.info()