# wave form 
def waveForm(arr):
    rows=len(arr)
    cols=len(arr[0])
    rarr=[[0 for col in range(cols)]for row in range(rows)]
    i=0
    for row in range(rows):
        if row%2==0:
            for col in range(cols):
                rarr[row][col]=arr[col][row]
        else:
            for col in range(cols-1,-1,-1):
                
                rarr[row][i]=arr[col][row]
                i+=1
            i=0    
       
    return rarr

arr=[[3,7,9,17],
     [6,8,3,8],
     [4,11,2,5],
     [2,5,1,9]]    
wf=waveForm(arr)   
print(wf) 