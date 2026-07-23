# arr = [1,5,3,7,2]
# ans =[]
# n = len(arr)
# target = 9
# for i in range(0,n):
#     for j in range(i+1,n):
#         if (arr[i] + arr[j]) == target:
#             ans.append(i)
#             ans.append(j)
#             print(ans)


arr = [1,5,3,7,2]
arr.sort()
ans =[]
n = len(arr)
target = 9
i = 0
j = n-1
while i<j:
    result = arr[i] + arr [j]
    if result > target:
        j -= 1
    elif result < target:
        i += 1
    else:
        ans.append(i)
        ans.append(j)
        print(ans)
        break