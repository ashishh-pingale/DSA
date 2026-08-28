def search(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2

        if target == nums[mid]:
            return mid
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

nums = [4,5,6,7,0,1,2]
target = 0

print(search(nums,target))


