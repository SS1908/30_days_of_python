arr = [22,56,1,34,2,98,5,65,9]

print("unsorted list is")
print(arr)

for i in range(len(arr)-1):
    swaped = False
    for j in range(i+1,len(arr)):
        if arr[j] < arr[i]:
            arr[i],arr[j] = arr[j],arr[i]
            swaped = True
    if swaped == False:
        break
print("sorted is using bubble sort")
print(arr)