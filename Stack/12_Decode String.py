def decodeString(s):
    stack = []
    num = 0
    current = ""

    for char in s:

        if char.isdigit():
            num = num * 10 + int(char)

        elif char == "[":
            stack.append((num, current))
            num = 0
            current = ""

        elif char == "]":
            repeat, previous = stack.pop()
            current = previous + current * repeat

        else:
            current += char

    return current


s = "3[a]2[bc]"
print(decodeString(s))