# find square root of numbers
def square_root(num):
    i=1
    while(True):
        if i*i == num:
            return i
        elif i*i<num and  (i+1)*(i+1)>num:
            return i
        i+=1
    return -1
sr=square_root(130)    
print(sr)
