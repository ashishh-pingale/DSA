def largestInteger(nums, k):
    count = {}

    # Check every subarray of size k
    for i in range(len(nums) - k + 1):
        seen = set()

        for j in range(i, i + k):
            seen.add(nums[j])

        # Each number should be counted only once
        # for this particular subarray
        for x in seen:
            count[x] = count.get(x, 0) + 1

    ans = -1

    for x in count:
        if count[x] == 1:
            ans = max(ans, x)

    return ans

nums = [3,9,2,1,7]
k = 3
print(largestInteger(nums,k))