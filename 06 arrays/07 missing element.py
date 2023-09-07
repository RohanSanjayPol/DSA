# missing element in array
def missing_element(arr):
    sum=0
    total=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    n=len(arr)+1
    total=n*(n+1)//2
    missing=total-sum
    return missing   

arr=[1,2,3,5]  
me=missing_element(arr)
print(me)

