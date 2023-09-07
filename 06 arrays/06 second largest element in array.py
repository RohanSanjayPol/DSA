# second largest element in the array
def second_largest(arr):
    largest=-1
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    second_largest_elem=-1
    for i in range(len(arr)):
        if arr[i]!=largest:
            if arr[i]>second_largest_elem:
                second_largest_elem=arr[i]
    return second_largest_elem 
arr=[1,2,3,4,5,6,7,8]
sl=second_largest(arr)
print(sl)           
