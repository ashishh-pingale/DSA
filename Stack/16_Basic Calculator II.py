def calculate(s):
    stack = []
    num = 0
    prev_op = '+'

    for i, ch in enumerate(s):

        if ch.isdigit():
            num = num * 10 + int(ch)

        if ch in "+-*/" or i == len(s) - 1:

            if prev_op == '+':
                stack.append(num)

            elif prev_op == '-':
                stack.append(-num)

            elif prev_op == '*':
                stack.append(stack.pop() * num)

            elif prev_op == '/':
                a = stack.pop()
                result = abs(a) // num
                if a < 0:
                    result = -result
                stack.append(result)

            prev_op = ch
            num = 0

    return sum(stack)

s = "3+2*2"
print(calculate(s))