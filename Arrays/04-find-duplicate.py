def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return arr[i]
    return -1


num = [1,2,4,6,2,7,8]
print(duplicate(num))



