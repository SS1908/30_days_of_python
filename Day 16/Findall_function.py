#The findall() function returns a list containing all matches.

import re


str = "The train in Spain"
x = re.findall("Sp",str)
print(x)

y = re.findall("ai",str)
print(y)

#If no matches are found, an empty list is returned
z = re.findall("india",str)
print(z)
