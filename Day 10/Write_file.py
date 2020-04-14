"""
    To write to an existing file, you must add a parameter to the open() function:

        "a" - Append - will append to the end of the file

        "w" - Write - will overwrite any existing content

Example

"""

#use parameter 'w' to write a content in a file.

f = open("fruits.txt","w")
f.write("charry") #it will overwrite a content of a file.
f.close()

f1 = open("fruits.txt","r")
print(f1.read())
f.close()

#use parameter 'a' to append a content at the end of file.

f2 = open("fruits.txt","a")
f2.write("mango")
f2.close()

f3 = open("fruits.txt","r")
print(f3.read())
f3.close()
