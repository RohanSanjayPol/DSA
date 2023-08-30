# reverse the number
def reverse_number(n):
    sum=0
    if n<0:
       sign=-1
    else:
       sign=1   
    n=abs(n)
       
    while(n!=0):
      rem=n%10
      n=n//10
      i=0
      sum=10*sum+rem
    sum=sum*sign  
    return sum
    
rn=reverse_number(-1234)    
print(rn)