# prefix sum

def prefixSum(arr):
    preArr=[]
    start=0
    end=1
    preArr.append(arr[0])
    while(end<=len(arr)-1):
        preArr.append(preArr[start]+arr[end])
        start+=1
        end+=1
    return preArr

arr=[6,4,5,-3,2,8]
pfs=prefixSum(arr)
print(pfs)    
