def max_avg(arr):
    k = 4
    window_sum = 0
    
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum

    for j in range(k,len(arr)):
        window_sum = window_sum + arr[j] - arr[j-k]
        max_sum = max(max_sum,window_sum)

    avg = (max_sum/k)

    return avg


nums = [1, 12, -5, -6, 50, 3]
print(max_avg(nums))
        
