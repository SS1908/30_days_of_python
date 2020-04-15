"""
    Python allows us to not declare the function in the standard manner.
    i.e.by using the def keyword.
    Rather, the anonymous functions are declared by using lambda keyword.

    syntax:  lambda argument : expression

"""

sum = lambda a,b:a+b
print("sum = ",sum(10,20))

def table(n):
    return lambda a:a*n;
n = int(input("enter a number "))
b = table(n)
for i in range(1,11):
     print(n,"X",i,"=",b(i))

