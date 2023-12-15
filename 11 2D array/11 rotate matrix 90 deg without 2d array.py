# rotate array 90 deg without 2d array

def rotateMat(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            matrix[col][row]=matrix[(rows-1)-row][col]