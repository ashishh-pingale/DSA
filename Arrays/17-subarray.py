arr = [1, -2, 3, -4, 5]
n=5
for start in range(0,n+1):
    for end in range(start,n+1):
        for k in range(start,end):
            print(arr[k],end="")
            
        print(end=" ")