# two sum problem using binary search

def twoSum(arr,target):
    for i in range(0,len(arr)-1):
        start=i+1
        end=len(arr)-1
        x=abs(target-arr[i])
        while(start<=end):
            mid=(start+end)//2
            if arr[mid]==x:
                return [i,mid]
            elif arr[mid]<x:
                start=mid+1
            else:
                end=mid-1
    return -1

arr=[2,7,11,15,27]   
ts=twoSum(arr,22)    
print(ts)                      
