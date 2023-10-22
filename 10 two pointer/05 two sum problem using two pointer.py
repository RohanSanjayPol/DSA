# two sum problem using two pointer

def twoSum(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        if arr[start]+arr[end]==target:
            return [start,end]
        elif arr[start]+arr[end]>target:
            end-=1
        else:
            start+=1
    return -1   
arr=[2,7,11,15,27]   
ts=twoSum(arr,22)    
print(ts)         