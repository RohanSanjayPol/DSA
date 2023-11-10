# trapping rain water

def trap(height):
    maxLeft=[]
    maxRight=[]
    minimum=[]
    trapArr=[]
    maxL=0
    maxR=0
    n=len(height)
    for i in range(0,n):
        if maxL<height[i]:
            maxL=height[i]
        maxLeft.append(maxL)
    for i in range(n-1,-1,-1):
        if maxR<height[i]:
            maxR=height[i]
        maxRight.append(maxR)

    start=0
    end=len(maxRight)-1
    while(start<=end):
        maxRight[start],maxRight[end]=maxRight[end],maxRight[start]
        start+=1
        end-=1

    for i in range(0,n):
        minimum.append(min(maxLeft[i],maxRight[i])) 

    for i in range(0,n):
        if height[i]>minimum[i]:
            trapArr.append(0)
        else:
            trapArr.append(minimum[i]-height[i])    

    return maxLeft,maxRight,minimum,trapArr         


arr=[0,1,0,2,1,0,1,3,2,1,2,1] 
print('arr',arr)
l,r,m,t=trap(arr)
print('max left',l)
print('max right',r)
print('minimum',m)
print('trapped water',t)
   
