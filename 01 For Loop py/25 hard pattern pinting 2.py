# hard pattern printing 2

for row in range(1,6):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(row):
        print(row,end=' ')
    print()        