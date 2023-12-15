# rotate matrix 90 degree

def rotateMatrix(matrix):
    rows=len(matrix)-1
    cols=len(matrix[0])
    Row=0
    rotaMat=[[0 for col in range(cols)] for row in range(rows,-1,-1)]
    for row in range(rows,-1,-1):
        for col in range(cols):
            rotaMat[col][row]=matrix[Row][col]
        Row+=1
    return rotaMat
matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
rm=rotateMatrix(matrix)  
print(rm)     