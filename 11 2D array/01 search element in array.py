# search element in array

def searchElem(arr,target):
    r=len(arr)
    c=len(arr[0])
    for row in range(r):
        for col in range(c):
            if arr[row][col]==target:
                return [row,col]
    return -1
  

arr=[[1,2,3],
     [4,5,6],
     [7,8,9],
     [10,11,12]
     ] 
se=searchElem(arr,6)
print(se)   