def sort_in(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
        return True
    
array = [1,2,3,4,5,6]
if sort_in(array):
    print("sorted array")
else:
    print("non sorted")
