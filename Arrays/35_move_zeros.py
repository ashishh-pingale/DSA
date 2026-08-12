def move(nums):
    left = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[left] , nums[i] = nums[i] , nums[left]

            left += 1
    return nums

nums = [0,1,0,3,0,12]
print(move(nums))