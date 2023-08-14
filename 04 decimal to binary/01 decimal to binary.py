# decimal to binary
def decimal_to_binary(n):
    ans=0
    for i in range(0,n,1):
        rem=n%2
        n=n//2
        ans=rem*10**i+ans
    return ans

dtb=decimal_to_binary(10)
print(dtb)

