# rotate matrix 180 degree

def rotateMatrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    Row=3
    rotmat=[[0 for col in range(cols)]for row in range(rows)]
    for row in range(rows):
        Col=0
        for col in range(cols-1,-1,-1):
            rotmat[Row][Col]=matrix[row][col]
            Col+=1
        Row-=1
        
        
    return rotmat
matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

rm=rotateMatrix(matrix)
print(rm)        