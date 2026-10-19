def targetIndices(nums, target):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if nums[i] == target:
            ans.append(i)

    return ans

nums = [1,2,5,2,3]
target = 2

print(targetIndices(nums,target))