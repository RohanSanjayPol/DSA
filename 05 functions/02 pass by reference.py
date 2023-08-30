# pass by reference
def swap(a,b):
    c=a
    a=b
    b=c

a=10,b=12
swap(a,b) 
print('a:',a,'b:',b)   