# largets sum of contigous sub array  - using Kadans algorithm
import sys
def largestSum(arr):
    prefix=0
    maxi=-sys.maxsize-1
    for i in range(len(arr)):
        prefix=prefix+arr[i]
        maxi=max(prefix,maxi)
        if prefix<0:
            prefix=0
    return maxi
arr=[3,4,-5,8,-12,7,6,-2]        
ls=largestSum(arr)
print(ls)
