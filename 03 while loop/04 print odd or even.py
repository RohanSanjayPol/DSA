# print odd or even
def odd_or_even(n):
    i=1
    odd=[]
    even=[]
    while i<=n:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
        i+=1
    return even,odd   

even,odd=odd_or_even(30)     
print('even',even)
print('odd',odd)          