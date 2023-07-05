# sum of n natural numbers

def sum_natural_numbers(n):
    sum=0
    for i in range(1,n+1,1):
        sum=sum+i
    return sum
snn=sum_natural_numbers(6) 
print(snn)   

def sum_of_natural_numbers(n):
    n=n*(n+1)/2
    return int(n)
sonn=sum_of_natural_numbers(6)
print(sonn)