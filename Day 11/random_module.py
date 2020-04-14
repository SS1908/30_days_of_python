"""
    random.random() :-    This function generates a random float number between 0.0 and 1.0.
    random.randiant() :-  This function returns a random integer between the specified integers.
    random.randrange() :- This function returns a randomly selected element from the range created by the start, stop, and step arguments. Value of start is 0 by default.
    random.choice() :-    This function returns a randomly selected element from a non-empty sequence.
    random.suffule() :-   This function randomly reorders the elements in the list.

"""
import random

x=random.random()
print(x)

y = random.randrange(1,100)
print(y)

list1 = [54,12,25,84,51]
z = random.choice(list1)
print(z)

