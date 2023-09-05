# search element in array
def search_elem(arr,elem):
    for i in range(0,len(arr)):
        if elem==arr[i]:
            return i
    return 'not found'
arr=[12,23,45,34,6,45,34]
sl=search_elem(arr,6)
print(sl)    