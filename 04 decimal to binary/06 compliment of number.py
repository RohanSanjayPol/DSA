# compliment of number
def compliment_of_number(n):
    sum=0
    i=0
    while(n>0):
        rem=n%2
        n=n//2
        if rem==0:
            rem=1
        else:
            rem=0    
        sum=2**i*rem+sum
        i+=1
    return sum    
cfn=compliment_of_number(8)
print(cfn)

        
