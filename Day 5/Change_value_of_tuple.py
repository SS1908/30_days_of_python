#   You cannot add items to a tuple:
#   thistuple = ("apple", "banana", "cherry")
#   thistuple[3] = "orange" # This will raise an error
#   print(thistuple)

tuple1 = ("sagar","meet","jt")
print(tuple1)

list1 = list(tuple1)
list1[1]="jay"
tuple1 = tuple(list1)
print(tuple1)