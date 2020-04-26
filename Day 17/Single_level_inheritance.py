class A:

    def feature1(self):
        print("Feature-1 of class A")

    def feature2(self):
        print("Feature-2 of class A")

#we are inheritingin class-A
class B(A):
    def feature3(self):
        print("Feature-3 of class-B")

    def feature4(self):
        print("Feature-4 of class-B")


#Now,we can acess methods and attributes of class-A using instance of class-B
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()