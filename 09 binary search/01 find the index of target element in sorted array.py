# find the index of target element in sorted array

def targetElement(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1
arr=[1,3,5,7,9,11]
te=targetElement(arr,9)  
print(te)          
