def subarray(nums,k):
    prefix_sum = 0
    prefix_freq = {0:1}
    count = 0

    for num in nums:
        prefix_sum += num
        needed = prefix_sum - k

        if needed in prefix_freq:
            count += prefix_freq[needed]
        prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1

    return count

nums = [1,1,1]
k = 2

print(subarray(nums,k))