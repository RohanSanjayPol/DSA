# 3 sum using brute force approach

def Sum3(arr,tar):
    n=len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==tar:
                    return [i,j,k]
        return -1        
arr=[1,4,45,6,10,8]                
s3=Sum3(arr,13)
print(s3)
