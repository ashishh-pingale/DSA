arr = [3,-4,5,4,-1,7,-8]
curr = 0
max_sum = float('-inf')

for i in arr:
    curr = curr + i
    max_sum = max(curr, max_sum)

    if curr < 0:
        curr = 0

print(max_sum)