arr = [1,1,0,1,1,1]
count = 0
max_count = 0
for i in range(len(arr)):
    if arr[i] == 1:
        count = count + 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)