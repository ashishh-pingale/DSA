def asteroidCollision(asteroids):
    stack = []

    for current in asteroids:
        while stack and stack[-1] > 0 and current < 0:

            if stack[-1] > abs(current):
                current = 0
                break
            elif stack[-1] == abs(current):
                stack.pop()
                current = 0
                break
            else:
                stack.pop()
        if current != 0:
            stack.append(current)
    return stack

asteroids = [5,10,-5]
print(asteroidCollision(asteroids))