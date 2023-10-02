# find the count of target elements in sorted array

def targetElementCount(arr,target):
    start=0
    end=len(arr)-1
    leftCount=0
    rightCount=0
    # left count
    while start<=end:
        mid=(start+end)//2
        if arr[mid]== target:
            end=mid-1
            leftCount=leftCount+1
        elif arr[mid]<target:
            start=mid+1
        else:
            end=end-1
    # right count
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            start=mid+1
            rightCount=rightCount+1
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    count=leftCount+rightCount-1
    return count  
arr=[1,2,2,2,3,4]     
lo=targetElementCount(arr,2)
print(lo)                               