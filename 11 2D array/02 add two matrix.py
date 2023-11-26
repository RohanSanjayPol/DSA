# add two matrix

def addMatrix(mat1,mat2):
    rows=len(mat1)
    cols=len(mat1[0])

    mat3=[[0 for c in range(cols)]for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            mat3[r][c]=mat1[r][c]+mat2[r][c]
    return mat3        

mat1=[[1,2,3],
      [4,5,6],
      [7,8,9]]
mat2=[[1,2,3],
      [4,5,6],
      [7,8,9]]
am=addMatrix(mat1,mat2)
print(am)