# suffix sum

def suffixSum(arr):
    sufArr=[]
    start=len(arr)-1
    end=len(arr)-2
    sufArr.append(arr[start])
    start=0
    while(end>=0):
        sufArr.append(sufArr[start]+arr[end])
        start+=1
        end-=1
    return sufArr   

arr=[6,4,5,-3,2,8]
sfs=suffixSum(arr)
print(sfs) 