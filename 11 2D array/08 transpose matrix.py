# transpose matrix

def transposeMatrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    transMatrix=[[0 for col in range(cols)] for row in range(rows) ]
    for row in range(rows):
        for col in range(cols):
            transMatrix[col][row]=matrix[row][col]
    return transMatrix

matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
tm=transposeMatrix(matrix)
print(tm)        
