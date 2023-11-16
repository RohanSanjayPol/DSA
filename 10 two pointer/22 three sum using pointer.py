# 3 sum using pointer

def threeSum(arr,target):
    n=len(arr)
    end=len(arr)-1
    for i in range(0,n-1):
        x=target-arr[i]
        start=i+1
        while(start<=end):
            if arr[start]+arr[end]==x:
                return [i,start,end]
            elif arr[start]+arr[end]>x:
                end-=1
            else:
                start+=1
    return -1
arr=[1,4,6,8,10,45] 
ts=threeSum(arr,24) 
print(ts)              
        
