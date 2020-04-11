"""
    To create a new file in Python, use the open() method, with one of the following parameters:

        "x" - Create - will create a file, returns an error if the file exist

        "a" - Append - will create a file if the specified file does not exist

        "w" - Write - will create a file if the specified file does not exist

"""

f = open("bike.txt","x") #this will creat a flie 'bike.txt'.
                        #you can pass parameter 'w'also.
f.close()