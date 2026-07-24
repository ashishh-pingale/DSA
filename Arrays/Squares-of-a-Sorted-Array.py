def square_sorted(arr):
    i = 0
    j = len(arr) - 1
    pos = len(arr) - 1
    result = [0] * len(arr)

    while i <= j:
        if abs(arr[i]) > abs(arr[j]):
            result[pos] = arr[i] ** 2
            i += 1
        else:
            result[pos] = arr[j] ** 2
            j -= 1
        pos -= 1

    return result

arr = [-7, -3, 2, 3, 11]
print(square_sorted(arr))

