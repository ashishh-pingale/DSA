def speed(nums,h): 
    left = 1
    right = max(nums)


    while left < right:
        mid = left + (right - left) // 2

        total_hours = 0

        for piles in nums:
            total_hours += -(-piles // mid)

        if total_hours <= h:
            right = mid
        else:
            left = mid + 1

    return left

nums = [3,6,7,11]
h = 8
print(speed(nums,h))