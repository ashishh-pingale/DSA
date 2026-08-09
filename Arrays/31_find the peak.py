def peak(nums):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
        if left == right:
            return nums[left]

nums = [1,2,3,1]
print(peak(nums))