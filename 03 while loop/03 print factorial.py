def factorial(n):
    fact=[]
    i=1
    while i<=n:
        if n%i==0:
            fact.append(i)
        i+=1
    return fact

f=factorial(30)      
print(f)  