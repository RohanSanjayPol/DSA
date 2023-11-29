# print row index with maximum sum

def maxSum(arr):
    rows=len(arr)
    cols=len(arr[0])
    rowSum=0
    maxi=0
    index=0
    for row in range(rows):
        for col in range(cols):
            rowSum=rowSum+arr[row][col]
        if rowSum>maxi:
            maxi=rowSum
            index=row
        rowSum=0
    return index

arr=[[1,3,6],
     [2,2,2],
     [3,3,6]
    ] 
ms=maxSum(arr) 
print(ms)      

