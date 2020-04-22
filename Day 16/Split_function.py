import re

#The split() function returns a list where the string has been split at each match.

str = "How are you How is everything"
x = re.split("\s",str)
print(x)


#You can control the number of occurrences by specifying the maxsplit parameter.

str1 = "How are you How is everything"
y = re.split("\s",str1,2)
print(y)