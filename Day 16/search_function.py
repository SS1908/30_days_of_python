import re
#The search() function searches the string for a match, and returns a Match object if there is a match.

str = "How are you. How is everything"
x = re.search("How",str)
print(x)

#If no matches are found, the value None is returned
y = re.search("how",str)
print(y)

print()
txt = "The rain in Spain"
z = re.search("^The.*Spain$",txt)
print(z)