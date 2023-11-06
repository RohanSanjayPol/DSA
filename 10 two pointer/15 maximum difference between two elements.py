# maximum differnce between two elements
import sys
def maxDiff(arr):
    maxi=-sys.maxsize-1
    diff=0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                diff=arr[j]-arr[i]
            maxi=max(diff,maxi)  
    return maxi
arr=[9,5,8,12,2,3,7,4]
md=maxDiff(arr)    
print(md)      


