"""
    Here, we have a three type of method inside a class.
     1) Instance method
     2) Class method
     3) Static method

"""

class student:

    school = "Sigma"

    #this is an instace method
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    #this is an instance method
    def get_avg(self):
        return (self.m1+self.m2+self.m3)/3

    #this is an classmethod
    #classmethod is define using "@classmethod"
    @classmethod
    def get_school(cls):
        print(cls.school)

    #this is an staticmethod
    #staticmethod is definr using "@staticmethod"
    @staticmethod
    def info():
        print("sigma international school")


s1 = student(33,56,85)
s2 = student(65,87,68)

#get the avrage of marks
print(s1.get_avg())
student.get_school()

print(s2.get_avg())
student.get_school()

#calling a static method of a class
student.info()
