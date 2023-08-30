# power of 2 
def power_of_two(n):
    while(n!=1):
        if n%2==1:
            return False
        n=n//2
    return True    
pft=power_of_two(31)
print(pft)