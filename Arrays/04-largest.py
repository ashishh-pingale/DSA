def largest(arr):
    largest = 0
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    print(largest)

arr = [1,45,65,34,67,19,78,45,11,34]
largest(arr)


