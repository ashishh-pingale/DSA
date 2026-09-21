def carFleet(target , speed , position):
    cars = list(zip(position , speed))
    cars.sort(reverse=True)

    stack = []

    for pos , spd in cars:
        time = (target - pos) / float(spd)

        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleet(target , speed , position))