"""
    You can define as many exception blocks as you want.
    e.g. if you want to execute a special block of code for a special kind of error
"""

try:
    print(x)
except NameError as e:
    print("x is not defined")
    print(e)
except ZeroDivisionError as e :
    print("you can not divide a number by zero")
except Exception as e:
    print(e)
finally:
    print("Everything looks fine!!! ")
