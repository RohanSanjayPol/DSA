# two pointer
def twoPointer(arr):
    start=0
    end=len(arr)-1
    while(start<=end):
        if arr[start]==0:
            start+=1
        elif arr[end]==1:
            end-=1
        else:
            arr[start],arr[end]=arr[end],arr[start]          
            start+=1
            end-=1
    return arr    

arr=[0,1,1,0,1,0,1]
tp=twoPointer(arr)
print(tp)