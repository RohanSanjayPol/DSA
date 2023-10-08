# find the index of target in rotated sorted array

def rotTargetElem(arr,target):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        if arr[start]<=arr[mid]:
            if arr[start]<=target<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if arr[mid]<target<=arr[end]:
                start=mid+1
            else:
                end=mid-1                
    return -1
arr=[4,5,6,7,0,1,2]
rte=rotTargetElem(arr,5)
print(rte)        
