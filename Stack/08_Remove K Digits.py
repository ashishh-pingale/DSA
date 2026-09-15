def remvoveK(nums,k):
    stack = []

    for digits in nums:
        while stack and k > 0 and stack[-1] > digits:
            stack.pop()
            k -=1
        stack.append(digits)

    if k > 0:
        stack = stack[:-k]

    result = "".join(stack).lstrip("0")

    return result if result else "0"
num = "1432219"
k = 3

print(remvoveK(num,k))
        