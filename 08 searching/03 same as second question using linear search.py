# find the correct index of sorted array

def using_linear_search(arr,target):
    lenght=len(arr)-2
    for i in range(0,lenght,1):
        if arr[i]==target:
            return i
        if target>arr[i] and target<arr[i+1]:
            return i+1
arr=[1,2,3,6,8,8,9]
uls=using_linear_search(arr,5) 
print(uls)       
