# advance pattern printing 5
for row in range(5,0,-1):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    for col in range(row-1,0,-1):
        print(col,end=' ')
    print()            