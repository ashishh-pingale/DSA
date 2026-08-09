def find(nums):
    left = 0 
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

        if left == right:
            return nums[right]

nums = [4,5,6,7,0,1,2]
print(find(nums))