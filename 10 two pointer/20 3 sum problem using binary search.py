# 3 sum problem using binary search

def b3Sum(arr,target):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            start=j+1
            end=len(arr)-1
            x=target-(arr[i]+arr[j])
            while(start<=end):
                mid=(start+end)//2
                if arr[mid]==x:
                    return [i,j,mid]
                elif arr[mid]<target:
                    end=mid-1
                else:
                    start=mid+1  
    return -1     

arr=[5,8,10,20,25,27,30,45,47,50] 
bs=b3Sum(arr,45)
print(bs)            
