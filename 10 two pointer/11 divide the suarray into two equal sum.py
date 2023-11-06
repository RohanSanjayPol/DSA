# divide the subarray into two equal sum

def equalSubArr(arr):
    total=0
    leftSubArr=0
    rightSubArr=0
    for i in range(len(arr)):
        total=total+arr[i]
    for i in range(len(arr)):
        leftSubArr=leftSubArr+arr[i]
        rightSubArr=total-leftSubArr
        if leftSubArr==rightSubArr:
            return [leftSubArr,rightSubArr]
    return-1

arr=[3,4,-2,5,8,20,-10,8]
esa=equalSubArr(arr) 
print(esa)   
