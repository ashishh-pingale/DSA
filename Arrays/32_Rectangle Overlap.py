def isRectangleOverlap(rec1, rec2):
    return (min(rec1[2], rec2[2]) > max(rec1[0], rec2[0]) and
            min(rec1[3], rec2[3]) > max(rec1[1], rec2[1]))

rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

print(isRectangleOverlap(rec1,rec2))