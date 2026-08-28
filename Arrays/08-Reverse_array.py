arr = [1,2,3,4,5,6]
size = 5
start = 0
end = size-1
while start<end:
    arr[start] , arr[end] = arr[end] , arr[start]
    start +=1
    end -=1
        
for i in arr:
    print(i , end=" ")