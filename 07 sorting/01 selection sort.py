# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        index=i
        for j in range(i+1,len(arr),1):
            if arr[j]<arr[index]:
                index=j
        arr[i],arr[index]=arr[index],arr[i]   
    return arr

arr=[12,43,1,23,6,4,8,87]
ss=selection_sort(arr) 
print(ss)    
