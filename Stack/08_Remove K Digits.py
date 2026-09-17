def removeKdigits(num, k):
    stack = []


    for digits in num:
        while stack and k > 0 and stack[-1] > digits:
            stack.pop()
            k -= 1
        stack.append(digits)
    if k > 0:
        stack = stack[:-k]
    result = "".join(stack).lstrip("0")

    return result if result else "0"

num = "10200"
k = 1

print(removeKdigits(num,k))