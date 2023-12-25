# longest palindrome

def longestPlindrome(str):
    # count of each element
    n=len(str)
    count=[]
    
    for i in range(n-1):
        val=1
        for j in range(i+1,n):
            if str[i]==str[j]:
                val+=1
        count.append(val)    
    return count        



str='naman'    
lp=longestPlindrome(str)
print(lp)