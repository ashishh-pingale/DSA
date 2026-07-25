def Three_sum(arr):
    arr.sort()
    result = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        j = i+1
        k = len(arr) - 1

        while j < k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < 0:
                j+=1
            elif sum > 0:
                k -= 1
            else:
                result.append([arr[i] , arr[j] , arr[k]])

                while j < k and arr[j] == arr[j+1]:
                    j += 1

                while j < k and arr[k] == arr[k-1]:
                    k -= 1

                j += 1
                k -= 1
    return result

arr =[-1,0,1,2,-1,-4]
print(Three_sum(arr))
                

     
    