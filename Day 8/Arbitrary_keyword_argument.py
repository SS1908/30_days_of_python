#when you don't know hom many keyword argument will be passed into a function add two asterisk "**" before parameter name.
#This way the function will receive a dictionary of arguments.

def function1(**name):
    print("hello "+name["name2"])

function1( name1 = "sagar" , name2="nayan" , name3="meet")