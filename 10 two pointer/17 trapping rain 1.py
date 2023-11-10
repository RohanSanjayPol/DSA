# trapping rainwater

def trap(arr):
    n=len(arr)
    leftMax=arr[0]
    rightMax=0
    trapWater=[0]
    for i in range(0,n):
        if arr[i]>rightMax:
            rightMax=arr[i]
    for i in range(1,n):
        current=arr[i]
        if current==arr[n-1]:
            trapWater.append(0)
        elif current==rightMax:
            leftMax=rightMax
            rightMax=0
            for j in range(current+1,n):
                if arr[j]>rightMax:
                    rightMax=arr[j]
            Min=min(leftMax,rightMax)
            if current>Min:
                trapWater.append(0)
            else:
                trapWater.append(Min-current)
        else:
            Min=min(leftMax,rightMax)
            if current>Min:
                trapWater.append(0)
            else:
                trapWater.append(Min-current)
            if current>leftMax:
                leftMax=current
    return trapWater  

arr=[0,1,0,2,1,0,1,3,2,1,2,1] 
trw=trap(arr)
print(arr)    
print(trw)          


           

