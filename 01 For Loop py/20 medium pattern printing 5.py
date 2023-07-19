# pattern printing
for row in range(1,6):
    for col in range(row):
        print(chr(96+row),end=' ')
    print()    