def missingMultiple(nums, k):
    seen = set(nums)

    multiple = k
    while multiple in seen:
        multiple += k

    return multiple

nums = [2,4,6,8,6,9]
k = 2
print(missingMultiple(nums,k))