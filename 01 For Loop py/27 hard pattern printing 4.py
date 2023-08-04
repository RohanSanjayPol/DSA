# hard pattern printing 4
for row in range(1,6):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(1,row+1):
        print(chr(96+col),end=' ')
    print()        