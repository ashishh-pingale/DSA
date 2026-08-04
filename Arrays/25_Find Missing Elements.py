def missingIntegers(nums):
    nums.sort()
    ans = []

    for i in range(len(nums) - 1):
        for x in range(nums[i] + 1, nums[i + 1]):
               ans.append(x)

    return ans

nums = [1,4,2,5]
print(missingIntegers(nums))
