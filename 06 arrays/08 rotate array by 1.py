# rotate array by 1
def rotate(arr,d):
    length=len(arr)-1
    temp=arr[length]
    for i in range(len(arr)-1,-1,-1):
        arr[i]=arr[i-d]

        if i==d-1:
            arr[i]=temp
    return arr 
    
       
arr=[1,2,3,4,5,6]
d=3
r=rotate(arr,d)
print(r)

