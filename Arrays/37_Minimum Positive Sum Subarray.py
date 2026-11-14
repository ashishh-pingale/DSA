class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            total = 0

            for j in range(i, min(i + r, n)):
                total += nums[j]
                length = j - i + 1

                if length >= l and total > 0:
                    ans = min(ans, total)

        return ans if ans != float('inf') else -1