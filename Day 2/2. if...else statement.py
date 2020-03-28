'''
The if...else statement evaluates test condtion and it will execute body of if
only when test condition is true.

Or if the condition evaluates false then body of else will be executed.

SYNTAX :
            if test_condition :
                    body of if;
            else :
                body of else;
'''

#Check a person can vote or not.
#min. age for vote is 18.


print("Enter your age : ")
age = int(input())
if age>=18 :
    print("you can vote")
else :
    print("your age is less than legal age to vote")
print("this line will always be executed")
