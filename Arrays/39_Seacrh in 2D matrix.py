def search(matrix,target):
    left = 0
    cols = len(matrix[0])
    right = len(matrix)*cols - 1

    while left <= right:
        mid = left + (right -  left) // 2
        row = mid // cols
        column = mid % cols

        if matrix[row][column] == target:
            return[row,column]
        elif matrix[row][column] < target:
            left = mid + 1
        else:
            right = mid - 1
            

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print(search(matrix,60))