# Maximum Sum Subarray of Size k

arr = list(map(int,input().split()))
k = int(input())

current = sum(arr[:k])
max_sum = current
for i in range(k,len(arr)):
    current = current - arr[i-k]
    current = current + arr[i]
    if max_sum < current :
            max_sum = current
print(max_sum)