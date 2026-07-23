def remove(nums):
    temp = []
    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            temp.append(i)
    for j in range(len(temp)):
        nums.pop(j)
    
    return nums

arr = [1,2,3,3,4,5,6,6,7,7,7,8,9,0]

remove(arr)