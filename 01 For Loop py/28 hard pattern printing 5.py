# hard pattern printing 5
for row in range(1,6):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(row,0,-1):
        print(col,end=' ')
    print()        
