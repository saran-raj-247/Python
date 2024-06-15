def insert_into_sorted_array(arr, item):
    
    if len(arr) >= 11:
        return arr
    
    
    arr.append(item)
    arr.sort()
    return arr
arr1= [int(input()) for i in range(10)]
item1 = int(input())
print("ITEM to be inserted:",item1,sep="")
print("After insertion array is:")
print(*insert_into_sorted_array(arr1, item1),sep="\n")
