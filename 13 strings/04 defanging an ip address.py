# defanging an IP address

def ipAddress(s):
    ans=''
    for i in s:
        if i=='.':
            ans+='[.]'
        else:
            ans+=i  
    return ans          
s='1.1.1.1'
ip=ipAddress(s)
print(ip)