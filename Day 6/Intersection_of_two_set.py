#using "&" operator
#intersection() method
#intersection_update() method


print(" & operator")
set1 = {"a","b","c"}
set2 = {"c","d","e"}
set3 = {"c","f","t"}

print(set1&set2)
print()

print("intersection() method")
print(set1.intersection(set2))
print()

print("intersection_update() method")
set1.intersection_update(set2,set3)
print(set1)
print()
