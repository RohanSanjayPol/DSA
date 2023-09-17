# binary search

# insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break  
    return arr          

def binary_search(arr,search):
    sorted_arr=insertion_sort(arr)
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if sorted_arr[mid]==search:
            return mid
        elif search<sorted_arr[mid]:
            end=mid-1
        else:
            start=mid+1
    return -1        

# main funtion
arr=[1,2,6,4,8,3,9]
bs=binary_search(arr,4) 
print(bs)               
