def trap_water(nums):
    left = 0
    right = len(nums) - 1
    total_water = 0
    left_max = 0
    right_max = 0

    while left < right:
        if nums[left] < nums[right]:
            left_max = max(left_max , nums[left])
            total_water += left_max - nums[left]
            left += 1
        else:
            right_max = max(right_max , nums[right])
            total_water += right_max - nums[right]
            right += 1

    return total_water

nums = [4,2,0,3,2,5]
print(trap_water(nums))