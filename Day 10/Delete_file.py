"""
To delete a file, you must import the OS module, and run its os.remove() function.

"""

#To avoid getting an error, you might want to check if the file exists before you try to delete it.
import os
f = open("months.txt","x")

if os.path.exists("months.txt"):
    os.remove()
else:
    print("file not exixts")