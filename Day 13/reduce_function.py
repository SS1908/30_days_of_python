from functools import reduce

num = [5,87,3,46,14,89,66,7]

#TODO find a even number from the list
even =list( filter(lambda a : a%2==0,num))
print(even)
print()

#TODO double all the even number

double = list(map(lambda n : n*2,even))
print(double)
print()

#TODO add all the avlues of double list
sum = reduce(lambda a,b:a+b,double)
print(sum)