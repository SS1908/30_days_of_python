#if statement in python.
#the body of the if executed only if the expression evaluates to true.

# SYNTAX:
#          if test_condition :
#                body of if;

'''
Check a person can vote or not.
min. age for vote is 18.
'''

print("Enter your age : ")
age = int(input())
if age>=18 :
    print("you can vote")
print("this line will always be executed")
