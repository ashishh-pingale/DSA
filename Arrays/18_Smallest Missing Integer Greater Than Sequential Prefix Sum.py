def missingInteger(nums):
    seen = set(nums)

    prefix_sum = nums[0]
    i = 1

    while i < len(nums) and nums[i] == nums[i - 1] + 1:
        prefix_sum += nums[i]
        i += 1

    while prefix_sum in seen:
        prefix_sum += 1

    return prefix_sum

nums = [3,4,5,1,12,14,13]
print(missingInteger(nums))
