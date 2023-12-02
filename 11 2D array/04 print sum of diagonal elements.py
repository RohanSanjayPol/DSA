# print sum of diagonal elements

def diagonalSumElem(arr):
    rows=len(arr)
    cols=len(arr[0])
    total=0
    for row in range(rows):
        total=arr[row][row]+total
    return total
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
dse=diagonalSumElem(arr)
print(dse)    
