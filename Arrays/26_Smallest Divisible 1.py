
def smallestNumber(n, t):
    while True:
        x = n
        product = 1

        while x > 0:
            product *= x % 10
            x //= 10

        if product % t == 0:
            return n

        n += 1

n = 10
t = 2
print(smallestNumber(n,t))
