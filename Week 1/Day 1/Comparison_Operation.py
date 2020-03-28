#Comparison Operator
#Comparison Operator is used to compare two values.
#it returns true or false

#   operator         name

#    ==             equal
#    !=             not equal
#    >              greater than
#    <              less than
#    >=             greater or equal to
#    <=             lesss or equal to

print("check number is equal or not")
num1 = 10
num2 = 3
print("a=",num1,"b=",num2)
print("num is equa :",num1==num2)

print()
print("!= operator")
num1 = 10
num2 = 3
print("a=",num1,"b=",num2)
print("num is not equal :",num1!=num2)

print()
print("> operator")
num1 = 10
num2 = 3
print("a=",num1,"b=",num2)
if num1>num2:
    print(num1," is greater")
else:
    print(num2," is greater")

print()
print("< operator")
num1=10
num2=3
print("a=",num1,"b=",num2)
if num1<num2:
    print(num1," is lesser")
else:
    print(num2,"is lesser")

print()
print(">= operator")
num1=10
num2=10
print("a=",num1,"b=",num2)
if num1>=num2:
    print(num1," is greater or equal")
else:
    print(num2,'is greater or equal')

print()
print("<= operator")
num1=10
num2=3
print("a=",num1,"b=",num2)
if num1<=num2:
    print(num1," is lesser or equal")
else:
    print(num2," is lesser or euqal")
