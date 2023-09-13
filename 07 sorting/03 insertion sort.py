# insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break    
    return arr            

arr=[12,2,3,23,5,1,4,7,23,54]
inser_sort=insertion_sort(arr) 
print(inser_sort)               