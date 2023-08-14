# binary to decimal
def binary_to_decimal(n):
    s=str(n)
    ans=0
    for i in range(len(s)):
        rem=n%10
        n=n//10
        ans=rem*2**i+ans
    return ans    
btb=binary_to_decimal(1100)
print(btb)


