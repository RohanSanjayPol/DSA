# fibonacci series
def fibonacci_series(n):
   last=0
   prev=1
   fibonacci_list=[]
   for _ in range(n):
      current=last+prev
      fibonacci_list.append(last)
      last=prev
      prev=current
      #fibonacci_list.append(current)
   return fibonacci_list

fs=fibonacci_series(10)  
print(fs)      
