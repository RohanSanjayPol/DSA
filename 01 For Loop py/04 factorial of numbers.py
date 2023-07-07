# factorial of numbers

def factorial_numbers(n):
    for i in range(n-1,0,-1):
        n=n*i
    return n
fn=factorial_numbers(5) 
print(fn)  
        
