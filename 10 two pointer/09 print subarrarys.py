# print sub arrays

def printSubArr(arr):
    size1=[]
    size2=[]
    size3=[]
    size4=[]
    for i in range(0,len(arr)):
        size1.append([arr[i]])
    
    for i in range(0,):
        if i<2:
            size2.append(arr[i])

    for i in range(0,len(arr),3):
        size3.append(arr[i])

    for i in range(0,len(arr),1):
        size4.append(arr[i])  

    return size1,size2,size3,size4          

arr=[4,3,7,2]
s1,s2,s3,s4=printSubArr(arr)
print('sub array of size 1 :',s1)  
print('sub array of size 2 :',s2)    
print('sub array of size 3 :',s3)    
print('sub array of size 4 :',s4)      