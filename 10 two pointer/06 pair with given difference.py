# pair with given difference 

def pairDiff(arr,diff):
    start=0
    end=1
    while(end<=len(arr)-1):
        if arr[end]-arr[start]==diff:
            return [start,end]
        elif arr[end]-arr[start]<diff:
            end+=1
        else:
            start+=1
    return -1        
arr=[2,3,5,10,50,80]          
pd=pairDiff(arr,45)
print(pd)  