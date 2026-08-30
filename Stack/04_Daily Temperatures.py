def daily_temperature(nums):
    stack = []
    ans = [0] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            ans[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return ans
temp = [73,74,75,71,69,72,76,73]

print(daily_temperature(temp))