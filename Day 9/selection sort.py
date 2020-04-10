import time
arr = [22,56,1,34,2,98,5,65,9]
print("unsorted list is ")
print(arr)

for i in range(len(arr)):

    min_index = i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index = j;
    arr[i],arr[min_index] = arr[min_index],arr[i]

print("sorted list using selection sort")
print(arr)



