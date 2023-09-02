# armstrong number
def armstrong_number(n):
    length=len(str(n))
    copy_n=n
    sum=0
    while(n>0):
        rem=n%10
        n=n//10
        sum=rem**length+sum
    if sum== copy_n:
        return True
    else:
        return False

an=armstrong_number(123) 
print(an)      
