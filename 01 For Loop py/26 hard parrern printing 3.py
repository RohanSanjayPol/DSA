# hard pattern printing 3
for row in range(1,6):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(col,end=' ')
    print()        