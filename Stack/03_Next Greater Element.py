def nextGreaterElement(nums1, nums2):
    stack = []
    ans = []
    next_greater = {}

    for i in range(len(nums2)-1,-1,-1):
        while stack and stack[-1] < nums2[i]:
            stack.pop()
        
        if not stack:
            next_greater[nums2[i]] = -1
        else:
            next_greater[nums2[i]] = stack[-1]
        stack.append(nums2[i])
        
    for num in nums1:
        ans.append(next_greater[num])
    return ans

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1,nums2))
        




