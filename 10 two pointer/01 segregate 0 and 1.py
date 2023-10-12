# segregate 0 and 1

def segregate0And1(arr):
    count0=0
    count1=0
    for i in range(len(arr)):
        if arr[i]==0:
            count0+=1
        else:
            count1+=1
    for i in range(count0):
        arr[i]=0
    for i in range(count0,len(arr)):
        arr[i]=1
    return arr    

arr=[0,1,1,0,1,0,1]
s=segregate0And1(arr)
print(s)