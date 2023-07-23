# pattern printing

for row in range(1,6):
    for col in range(5,5-row,-1):
        print(col,end= ' ')
        
    print()