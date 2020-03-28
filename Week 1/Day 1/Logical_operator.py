#Logical operators are use to combine conditional statements.
#     Operator      Description

#        and            Returns True if both statements are true
#        or             Returns True if one of the statements is true
#        not            Reverse the result, returns False if the result is true

print("and operator")
x=6
print(x)
if x>0 and x<10:
    print("number is between 0 to 10")
else:
    print("numer is not is between 0 to 10")

print()
print(" or opreator")
x=11
if x>0 or x<10:
    print("one or both conditons are true")
else:
    print("both the conditions are false")

print()
print("not operator")
x = True
print("before use of not operator x is",x)
print("after using not operator x is become",not x)
