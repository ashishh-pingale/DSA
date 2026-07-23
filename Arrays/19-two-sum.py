arr = [2,7,11,15]
target = 9
def two_sum(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False

print(two_sum(arr))