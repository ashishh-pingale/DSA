def Stock(arr):
    best_buy = arr[0]
    max_profit = 0
    for i in range(len(arr)):
        if arr[i] > best_buy:
            max_profit = max(max_profit,arr[i] - best_buy)
        best_buy = min(best_buy,arr[i])
    return max_profit

arr = [7,1,5,6,4]
print(Stock(arr))