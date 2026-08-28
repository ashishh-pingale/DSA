def reverse(nums , left , right):
    while left < right:
        nums[left] , nums[right] =  nums[right] , nums[left]
        left +=1
        right -=1
    return nums

arr = [1,2,3,4,5,6]
n = len(arr)
print(reverse(arr,0,n-1)) 