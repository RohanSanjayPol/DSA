# find how many zeros are present in factorial 
def count_zeros_factorial(n):
    count=0
    while n>=5:
        n=n//5
        count+=n
    return count    

f=count_zeros_factorial(25)    
print(f)  
