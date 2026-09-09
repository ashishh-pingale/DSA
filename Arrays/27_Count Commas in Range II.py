def countCommas(n):
    ans = 0
    p = 1000

    while p <= n:
        ans += n - p + 1
        p *= 1000

    return ans

n = 1002
print(countCommas(n))