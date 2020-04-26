class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        #we have a two methods to create a object of leptop class
        # 1)inside a __init__ method of super class
        self.lap = self.leptop()
        # 2)using instance of super class


    def show(self):
        print(self.name,self.rollno)

    #this is our Inner class
    class leptop:

        def __init__(self):
            self.cpu = "i7"
            self.ram = 8
            self.brand = "LENOVO"

        def show(self):
             print(self.cpu,self.ram,self.brand)


s1 = student("sagar",170220107009)
s1.show()
#accesing atrributes of sub-class using super-class object.
print(s1.lap.cpu,s1.lap.ram,s1.lap.brand)

# 2)using instance of super class
lap = student.leptop()
lap.show()
#we can also do this
#print(lap.cpu,lap.ram,lap.brand)