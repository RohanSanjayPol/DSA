# divide the subarray into two equal sum

def equalSum(arr):
    leftSubArr=0
    RightSubArr=0
    for i in range(0,len(arr)-1):
        leftSubArr=leftSubArr+arr[i]
        for j in range(i+1,len(arr)):
            RightSubArr=RightSubArr+arr[j]
        if leftSubArr==RightSubArr:
            return [[leftSubArr,RightSubArr]]
        RightSubArr=0
    return -1

arr=[3,4,-2,5,8,20,-10,8]
es=equalSum(arr) 
print(es)       
