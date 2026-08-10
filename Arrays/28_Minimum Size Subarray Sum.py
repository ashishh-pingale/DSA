def Minimum_Size_Subarray_Sum(nums,target):
    left = 0
    window_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            length = (right - left) + 1
            min_length = min(min_length,length)

            window_sum -= nums[left]
            left += 1

    if min_length == float('inf'):
        return 0


    return min_length

target = 7
nums = [2,3,1,2,4,3]
print(Minimum_Size_Subarray_Sum(nums,target))
        




    
