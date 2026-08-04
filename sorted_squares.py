# square the elemnts in the list and make them sorted without using any sorted function
# By using two pointers to solve it


arr = list(map(int,input().split()))

left = 0
right = len(arr)-1
pos = len(arr)-1

res =[0]*len(arr)


while left <= right :
    if abs(arr[left]) < abs(arr[right]):
        res[pos] = arr[right]**2
        right -= 1
        pos -= 1
    else:
        res[pos] = arr[left]**2
        left += 1
        pos -= 1
print(res)