#you can not copy a list simply by list1=list2
#there are two ways to copy a list
# 1. copy() method
# 2. list() method
#list() constructor is used to creat a list

print("copy() method")
name = ["sagar","meet","jt","nayan","dallu","divlo"]
frds = name.copy()
print(name)
print(frds)
print()

print("list() method")
name1 = ["sagar","meet","jt","nayan","dallu"]
print(name1)
frd = list(name1)
print(frd)
print()

name2 = list(("sagar","meet","jt","nayan"))
print(name2)