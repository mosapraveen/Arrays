# Take a array from user

arr = list(map(int,input().split()))

left = 0
for right in range(len(arr)):
    if arr[right] != 0 :
        arr[right] , arr[left] = arr[left] , arr[right]
        left+=1
        
print(arr)