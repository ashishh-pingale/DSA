def reverseDegree(s):
    ans = 0

    for i in range(len(s)):
        value = ord(s[i]) - ord('a') + 1
        reverse_value = 27 - value

        ans += reverse_value * (i + 1)

    return ans

s = "abc"
print(reverseDegree(s))