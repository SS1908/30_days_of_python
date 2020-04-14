"""
By default the read() method returns the whole text, but you can also specify how many characters you want to return.

"""

#read a 3 characters from the file.

f = open("car.txt","rt")
print(f.read(3))
f.close()


#read a line frome the file.

f = open("car.txt")
print(f.readline())  #it gives first line from the file.
print(f.readline())  #it gives second line from the file.
f.close()

#By looping throught file you can read whole file line by line.

f = open("car.txt")
for x in f:
    print( x )
