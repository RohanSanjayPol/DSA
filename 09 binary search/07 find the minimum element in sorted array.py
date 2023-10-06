# find the minimum element in sorted array
def reversedMinimumElem(arr):
    start=0
    end=len(arr)-1
    ans=arr[0]
    while(start<=end):
        mid=(start+end)//2
        if arr[0]<arr[mid]:
            start=mid+1
        else:
            ans=mid
            end=mid-1
    return ans     

arr=[4,5,6,7,0,1,2]
rme=reversedMinimumElem(arr)           
print(rme)