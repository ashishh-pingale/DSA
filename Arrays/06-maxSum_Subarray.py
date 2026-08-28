arr = [1, -2, 3, -4, 5]
current_Sum = 0
MaxSum = float('-inf')
for num in arr:
    current_Sum += num
    MaxSum = max(MaxSum, current_Sum)
    if current_Sum < 0:
        current_Sum = 0
print(MaxSum, end=" ")
print()
 