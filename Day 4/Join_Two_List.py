#There are three ways to join two lists.
# 1.Using '+' operator.
# 2.using append() methd.
# 3.using extend() method.

print("using + operator")
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)
print()

print("Using append() method")
list4 = ["ab","bc","cd"]
list5 = [4,5,6]
for x in list5:
    list4.append(x)
print(list4)
print()

print("using extend() method ")
list6 = ["a", "b" , "c"]
list7 = [1, 2, 3]

list6.extend(list7)
print(list6)
