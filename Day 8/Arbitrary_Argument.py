#Arbitrary argument are used when you dont know how many argument is to be passed.
#This way the function will receive a tuple of arguments

def function_sum(*args):
    a=args[0]+args[1]
    b=args[0]+args[1]+args[2]+args[3]
    print(a)
    print(b)
    
function_sum(5,10,25,36)