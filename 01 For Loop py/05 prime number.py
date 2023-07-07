# prime number

def prime_number(n):
    for i in range(2,n):
        if n%i==0:
            return 'not prime'
        else:
            return 'prime'
        
pn=prime_number(7)
print(pn)
           