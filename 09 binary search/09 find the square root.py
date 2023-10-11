# find the square root using binary search

def findSqrt(num):
    start=1
    end=num
    ans=-1
    while(start<=end):
        mid=(start+end)//2
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            ans=mid
            start=mid+1
        else:
            end=mid-1  
    return ans  
fs=findSqrt(99)
print(fs)        