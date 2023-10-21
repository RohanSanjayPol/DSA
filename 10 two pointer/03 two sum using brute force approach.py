# two sum problem using brute force approach

def twoSum(arr,target):
    for i in range(0,len(arr)-1):
        for j in range(i,len(arr)-1):
            if arr[i]+arr[j+1]==target:
                return [arr[i],arr[j+1]]
    return -1
arr=[2,7,11,15,27]
ts=twoSum(arr,22) 
print(ts)  