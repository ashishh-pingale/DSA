def binary_search(arr,target):
    for i in range(len(arr)):
        low = 0
        high = len(arr)-1

        while low<=high:
            mid = low + (high - low) //2
            if target == arr[mid]:
                return mid
            if target > arr[mid]:
                low = mid + 1
            else:
                high = mid-1
        return -1
            
arr = [1,45,65,34,67,19,78,45,11,34]

print(binary_search(arr,67))

    
    

