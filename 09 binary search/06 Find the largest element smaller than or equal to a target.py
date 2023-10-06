# Find the largest element smaller than or equal to a target
def largestTargetElement(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return arr[mid]
        elif arr[mid]<target:
            ans=arr[mid]
            start=mid+1
        else:
            end=mid-1
    return ans          
arr = [2,3,5,6,8]
lte=largestTargetElement(arr,4) 
print(lte)
