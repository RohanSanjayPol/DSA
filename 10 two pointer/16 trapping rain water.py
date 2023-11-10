# trapping rain water problem

def trap(arr):
    maxleft=arr[0]
    maxRight=0
    trappArr=[0]
    for i in range(0,len(arr)):
        if arr[i]>maxRight:
            maxRight=arr[i]
            maxRightIndex=i
    maxRight 

    for i in range(1,len(arr)):
        current=arr[i]
        if current>maxleft:
            maxleft=current

        if i>maxRightIndex:
            n=len(arr)-1 
            maxRight=arr[n] 
            Min=min(maxleft,maxRight)
              
        
        Min=min(maxleft,maxRight)
        trappArr.append(Min-arr[i])       

        
        
        

    return trappArr 
       

arr=[0,1,0,2,1,0,1,3,2,1,2,1] 
trw=trap(arr)
print(arr)    
print(trw)   