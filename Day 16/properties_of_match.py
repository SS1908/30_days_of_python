""""
    .span() returns a tuple containing the start-, and end positions of the match.
    .string returns the string passed into the function.
    .group() returns the part of the string where there was a match.
"""
import re

str = "The train in Spain"
x = re.search("train",str)
print(x.span())
print(x.string)
print(x.group())