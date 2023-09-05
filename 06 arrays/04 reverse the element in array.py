# reverse the element in array
def reverse(arr):
    rev=[]
    for elem in range(len(arr)-1,-1,-1):
        rev.append(arr[elem])
    return rev    
arr=[1,2,3,4,5,6,7,8,9]
r=reverse(arr)
print(r)
print(6//2)