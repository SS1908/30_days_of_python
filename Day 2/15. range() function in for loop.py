'''
range() function :
the range() function returns a sequence of number ,string from 0 by default,
And increment by 1 (by default) and ends at specified number

properties :
1) we can specify starting value by adding perameter. ex. range(2,10)
2)we can also specify step size by adding third parameter. ex. range(2,30,3)

'''

#print 10 natural number using for loop;
for i in range(11):
    print(i)

#print 10 natural number start from 3 using for loop;
print()
for j in range(3,11):
    print(j)

#print natural number less than 20,and increment step size is 2;
print()
for k in range(1,20,2):
    print(k)