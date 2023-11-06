# maximum sum of suarray
import sys
def maxSum(arr):
    maxi=-sys.maxsize-1
    for i in range(0,len(arr)):
        prefix=0
        for j in range(i,len(arr)):
            prefix=prefix+arr[j]
            maxi=max(prefix,maxi)
    return maxi       

arr=[4,-6,2,8] 
ms=maxSum(arr)
print(ms)

            
            
          