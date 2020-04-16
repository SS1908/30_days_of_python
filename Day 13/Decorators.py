def div(a,b):
    print(a/b)

def smart_div(fun):

    def inner_fun(x,y):
        if x < y :
            x,y = y,x
        return fun(x,y)
    return inner_fun

div1 = smart_div(div) #passing div function as a parameter in smart_div function.


div(2,4)  #calling div function.