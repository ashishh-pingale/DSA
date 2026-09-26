def findGCD(nums):
    a = min(nums)
    b = max(nums)

    while b:
        a, b = b, a % b

    return a

nums = [2,5,6,9,10]
print(findGCD(nums))