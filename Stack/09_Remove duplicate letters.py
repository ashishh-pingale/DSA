def removeDuplicateLetters(s):
    stack = []
    freq = {}
    seen = set()

    for i in range(len(s)):
        freq[s[i]] = freq.get(s[i],0) + 1

    for char in s:
        freq[char] -= 1
        if char in seen:
            continue
        while stack and stack[-1] > char and freq[stack[-1]] > 0:
            top = stack.pop()
            seen.remove(top)

        stack.append(char)
        seen.add(char)
    return "".join(stack)

s = "bcabc"
print(removeDuplicateLetters(s))

     

