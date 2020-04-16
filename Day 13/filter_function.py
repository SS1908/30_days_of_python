num = [5,87,3,46,14,89,66,7]

print("Using lambda function ")
even =list( filter(lambda a : a%2==0,num))
print(even)
print()

print("using simple function ")
def odd (n):
    return n%2!=0

oddlist = list(filter(odd,num))
print(oddlist)