#descard()
#remove()
#pop()
#clear()


print("descard() method")
#will not give an error although the kry is not found
Months = set(["January","February", "March", "April", "May", "June"])
Months.discard("January")
print(Months)
print()

print("remove() method")
#will give an error if key is not found
Months = set(["January","February", "March", "April", "May", "June"])
Months.remove("February")
print(Months)
print()

print("pop() method")
Months = set(["January","February", "March", "April", "May", "June"])
Months.pop()
print(Months)
print()

print("Clear() method")
Months = set(["January","February", "March", "April", "May", "June"])
Months.clear()
print(Months)