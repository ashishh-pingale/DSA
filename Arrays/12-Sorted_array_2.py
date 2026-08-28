def sorted_array(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i+1) % len(arr)]:
            count = count + 1
    if count <= 1 :
        return True
    else:
        return False
        



nums = [2,1,3,4]
print(sorted_array(nums))
