def largestRectangleArea(heights):
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()

            if stack:
                width = i - stack[-1] -1
            else:
                width = i

            height = heights[top]
            area = width * height
            max_area = max(max_area , area)
        stack.append(i)

    while stack:
        top = stack.pop()

        if stack:
            width = len(heights) - stack[-1] -1 
        else:
            width = len(heights)
        
        height = heights[top]
        area = width * height
        max_area = max(max_area , area)
    return max_area

heights = [2,1,5,6,2,3]

print(largestRectangleArea(heights))
        