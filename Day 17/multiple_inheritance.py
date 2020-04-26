class A:

    def feature1(self):
        print("Feature-1 of class A")

    def feature2(self):
        print("Feature-2 of class A")


class B:
    def feature3(self):
        print("Feature-3 of class-B")

    def feature4(self):
        print("Feature-4 of class-B")

#here class-A and class-B are independent classes.
#we inheriting class-A and class-B both.
class C(A,B):

    def feature5(self):
        print("Feature-5 of class-C")

    def feature6(self):
        print("Feature-6 of class-C")


if __name__=="__main__":

    """
    we can access methods and Attribute of class-A and Class-B using instance of class-C
    But we can not access methods and attribute of class-A using instance of class-B
    and visa-versa.
    """
    c1 = C()
    c1.feature1()
    c1.feature2()
    c1.feature3()
    c1.feature4()
    c1.feature5()
    c1.feature6()