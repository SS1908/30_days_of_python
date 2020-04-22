import re

#The sub() function replaces the matches with the text of your choice

str = "The train in Spain"
replaced = re.sub("train","car",str)
print(replaced)
print()

#You can control the number of replacements by specifying the count parameter
str1 = "How are you. How is everthing"
replaced1 = re.sub("How","wow",str1,1)
print(replaced1)
