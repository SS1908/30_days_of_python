"""
    List Comprehension is defined as an elegant way to define, create a list in Python.
    It consists of brackets that contains an expression followed by for clause.

    SIGNATURE:
                [ expression 'for' item 'in' list 'if' condition]
"""

letters = []
for letter in 'Python':
    letters.append(letter)
print(letters)
print()

#You can also do using list comprehension.
letters = [letter for letter in 'Python']
print(letters)  
