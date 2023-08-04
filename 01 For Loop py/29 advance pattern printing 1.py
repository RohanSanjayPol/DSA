# advance pattern printing 1
for row in range(1,6):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(1,(row*2-1)+1):
        print(col,end=' ')
    print()        