# find the minimum element in array
def minimum_value(arr):
    minimum=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<minimum:
            minimum=arr[i]
    return minimum
arr=[12,34,54,34,65,87,4,6,78]
mv=minimum_value(arr)
print(mv)        