def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates

num = [1,2,4,6,2,7,8]
print(find_duplicates(num))



