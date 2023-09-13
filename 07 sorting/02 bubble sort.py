# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        boolean=0
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                boolean=1
        if boolean==0:
            return arr    
    return arr
arr=[12,34,5,3,23,17,2]
bs=bubble_sort(arr)
print(bs)            