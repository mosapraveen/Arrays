# move zeroes to the end

n = int(input())
arr = list(map(int,input().split(" ")))

left = 0
for right in range(len(arr)):
    if arr[right] != 0 :
        arr[left] , arr[right] = arr[right] , arr[left]
        left+=1
print(arr)
