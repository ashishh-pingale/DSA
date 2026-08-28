def removeDuplicates(nums):
    if not nums:          # Edge case: empty array
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

arr = [1,2,3,3,4,5,6,6,7,7,7,8,9,0]

removeDuplicates(arr)
for i in range(0,10):
    print(i)
