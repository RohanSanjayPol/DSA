# spiral form

def spiralForm(arr):
    top=0
    bottom=5
    left=0
    right=5
    while(top<=bottom and left<=right):
        for i in range(left,right+1):
            print(arr[top][i],end=' ')
        print()    
        top+=1
        for j in range(top,bottom+1):
            print(arr[j][right],end=' ')
        print()    
        right-=1
        for k in range(right,left-1,-1):
            print(arr[bottom][k],end=' ')
        print()    
        bottom-=1
        for l in range(bottom,top-1,-1):
            print(arr[l][left],end=' ')
        print()    
        left+=1

arr=[[1,2,3,4,5,6],
     [7,8,9,10,11,12],
     [13,14,15,16,17,18],
     [19,20,21,22,23,24],
     [25,26,27,28,29,30],
     [31,32,33,34,35,36]]  
sf=spiralForm(arr)
print(sf)                  
