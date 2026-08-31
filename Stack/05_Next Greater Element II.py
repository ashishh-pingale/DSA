def next_greater(nums):
    stack = []
    ans = [-1] * len(nums)

    for i in range(2 * len(nums)):
        current_index = i % len(nums)

        while stack and nums[current_index] > nums[stack[-1]]:
            ans[stack[-1]] = nums[current_index]
            stack.pop()

            if i < len(nums):
                stack.append(current_index)
    return ans

