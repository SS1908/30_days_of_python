'''
if...elif..else statement used to check multiple condition and
divert the flow of program control

SYNTAX :
         if test_condition :
                body;
         elif test_condition :
                body;
         elif test_condition :
                body;
                .
                .
         else :
                body of else;
'''

#print a gread for user given marks

marks = int(input("Enter your marks"))

if marks >=90 :
    print("A")
elif marks >= 80 :
    print("B")
elif marks >= 70 :
    print("C")
else :
    print("DD")
