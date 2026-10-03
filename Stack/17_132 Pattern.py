def find132pattern(nums):
    stack = []
    second = float('-inf')

    for i in range(len(nums) - 1, -1, -1):

        if nums[i] < second:
            return True

        while stack and nums[i] > stack[-1]:
            second = stack.pop()

        stack.append(nums[i])

    return False

nums = [3,1,4,2]
print(find132pattern(nums))