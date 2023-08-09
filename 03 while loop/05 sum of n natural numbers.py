def sum_natural_numbers(n):
    sum=0
    i=1
    while i<=n:
        sum=sum+i
        i+=1
    return sum 
snm=sum_natural_numbers(30)
print(snm)