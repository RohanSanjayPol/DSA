# hard pattern printing
for row in range(1,6):
    for col in range(5-row):
        print(' ',end=' ')
    for col in range(row):
        print('*',end=' ')
    print()        