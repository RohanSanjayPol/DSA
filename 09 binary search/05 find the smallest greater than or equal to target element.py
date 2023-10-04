# find the smallest greater than or equal to target element
def targetElement(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            start=mid+1
        else:
            ans=arr[mid]
            end=mid-1
    return ans 
arr = [2,3,5,6,8]
te=targetElement(arr,4)  
print(te)     