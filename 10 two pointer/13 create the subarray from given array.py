# create the subarray from given array

def subArray(arr):
    subArr=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            subArr.append(arr[i:j+1])    
    return subArr
arr=[1,2,3]
sa=subArray(arr)
print(sa)        
            