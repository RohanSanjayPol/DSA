# print the number in reverse order
def reverse_number(n):
    for i in range(n,0,-1):
        print(i)

reverse_number(10)  

# print the odd numbers
def odd_numbers(n):
    for i in range(1,n+1,2):
        print(i,end=' ')
odd_numbers(10) 
print()

# print table 
def table(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i)

table(3)    

# power 
def power(n,pow):
    mul=1
    for i in range(pow,0,-1):
        n=n*i
    return n    

p=power(5,4)  
print(p)   

# print the multiplication of 5 for 4 times
def mul(number,n):
    i=number
    for _ in range(n):
        number=number*i
    return number

m=mul(5,4)  
print(m)      

