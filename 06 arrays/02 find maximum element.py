# find maximum element
def max_element(arr):
    maximum=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
    return maximum
arr=[12,23,43,54,2,378,54]
ml=max_element(arr)
print(ml)        