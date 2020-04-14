"""
    We can import a module named ' datetime ' to work with date and time as date object;

    Formate code                discription             example
    %a                           weekday , sort          tue
    %A                           weekday , full          tuesday
    %b                           month , sort            dec
    %D                           month , full            december
    %y                           year , sort             18
    %Y                           year , full             2018

"""
import datetime

#print current date and time
print(datetime.datetime.now())

#print weekday of today
x= datetime.datetime.now()
print(x.strftime("%A"))
print(x.strftime("%a"))

