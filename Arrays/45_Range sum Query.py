def prefix_sum(nums):
    prefix = [0]

    for num in nums:
        prefix.append(prefix[-1] + num)

    return prefix


def range_sum(nums, left, right):
    prefix = prefix_sum(nums)
    return prefix[right + 1] - prefix[left]

nums = [2, 4, 6, 8, 10]
print(range_sum(nums, 1, 3))