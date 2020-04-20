"""

The finally block, if specified, will be executed regardless if the try block raises an error or not.

"""
a=5
b=2

try:
    print(a/b)

except:
    print("you can not divide a number by zero")

finally:
    print("Everything is Alright")

    #generally we use a finally block for closing a files and connections
    #finally block use for clean up a resources
