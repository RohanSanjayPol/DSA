# decimal to binary
def decimal_to_binary(n):
    sum=0
    i=0
    while(n>0):
        rem=n%2
        n=n//2
        sum=rem*10**i+sum
        i+=1
    return sum
dtb=decimal_to_binary(10)    
print(dtb)