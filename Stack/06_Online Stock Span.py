def span(stock):
    stack = []
    ans = []

    for i in range(len(stock)):
        while stack and stack[-1][1] <= stock[i]:
            stack.pop()

        if stack:
            span = i - stack[-1][0]
        else:
            span = i + 1
        ans.append(span)
        stack.append((i , stock[i]))
    return ans
        
