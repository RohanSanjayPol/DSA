# returning unique elements

def unique_elements(arr):
    lenght=len(arr)
    unique=set(arr)
    unique_list=list(unique)
    len_unique=len(unique)
    fill=lenght-len_unique
    for _ in range(0,fill):
        unique_list.append('_')
    return unique_list
arr=[12,23,12,1,1,5,6,5,12]
ue=unique_elements(arr)
print(ue)