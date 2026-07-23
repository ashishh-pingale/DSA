def linear_search(arr ,target) :
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
            
arr = [1,45,65,34,67,19,78,45,11,34]

print(linear_search(arr,67))

    
    