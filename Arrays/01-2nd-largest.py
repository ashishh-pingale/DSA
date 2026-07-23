def secLarge(arr):
    large = 0
    secLarge = 0
    for i in range(len(arr)):
        if arr[i] > large:
            secLarge = large
            large = arr[i]

    print(f"The largest number is : {large}")
    print(f"The Second largest number is : {secLarge}")

arr = [1,45,65,34,67,19,78,45,11,34]
secLarge(arr)