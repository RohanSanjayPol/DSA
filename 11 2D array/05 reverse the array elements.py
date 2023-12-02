# reverse the 2d array elements

def reverseElem(arr):
    rows=len(arr)
    for row in range(rows):
        start=0
        end=len(arr[0])-1
        while(start<=end):
            arr[row][start],arr[row][end]=arr[row][end],arr[row][start]
            start+=1
            end-=1
        
    return arr
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
re=reverseElem(arr)        
print(re)
