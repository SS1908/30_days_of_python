# Take a list and store a square of all the element in another list.

#General approach
print("General aprroch")
list1 = [1,2,3,4,5,6]
list2 = []
for i in list1:
    list2.append(i*i)
print(list2)
print()

#Using List Coprehention
print("Using List Coprehention")
list3 = [1,2,3,4,5,6]
list4 = [n*n for n in list3 ]
print(list4)
print()

#IF condition in list comprehension
print("Using List Coprehention")
list5 = [1,2,3,4,5,6]
list6 = [n*n for n in list5 if n%2==0]
print(list6)
print()