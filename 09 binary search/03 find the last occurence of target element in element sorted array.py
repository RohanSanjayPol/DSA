# find the last occurence of target element in sorted array

def lastOccurence(arr,target):
    start=0
    end=len(arr)-1
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            ans=mid
            start=mid+1
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return mid
arr=[1,2,2,2,3,4]     
lo=lastOccurence(arr,2)
print(lo)                  