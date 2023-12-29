# rotate the string by two place

def rotateString(st,rot):
    li=[]
    n=len(st)
    for i in range(rot):
        li.append(st[n-i-1])
    for i in range(n,-1,-1):
        st[n]=st[n-rot]
    for i in range(rot):
        st[i]=st[rot-i-1] 

    return st

st='rohan'
rs=rotateString(st,2) 
print(rs)  



