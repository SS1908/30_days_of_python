#You can delete properties on objects by using the 'del' keyword

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name,end=" ")
        print(self.age)

s1 = student("sagar",21)
s2 = student("JT",20)

print("before deleting")
s1.info()
s2.info()
print()

del s2.age
print("after deleting a age of JT")
s1.info()
s2.info() #it will gives you an error,"object has no attribute"
         #because s2 object have no attribute called age.