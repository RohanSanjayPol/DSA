# find the index of element which is not present

def fun(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        #if target>arr[mid] and target<arr[mid+1]:
           # return mid+1
        
        elif target> arr[mid]:
            start=mid+1
        else:
            end=mid-1 
    return start        
arr=[1,2,3,6,8,8,9]
f=fun(arr,7)
print(f)              