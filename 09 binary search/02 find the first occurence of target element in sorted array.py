# find first occurence of target element in sorted array
def firstOcurrence(arr,target):
    start=0
    end=len(arr)-1
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            ans=mid
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return ans   
arr=[1,2,2,2,3,4]     
fo=firstOcurrence(arr,2)
print(fo)            
