n=int(input())
arr = list(map(int,input().split(",")))


high = -1
sec = -1

for i in range(len(arr)):
    if arr[i] > high :
        high = arr[i]
        
for i in range(len(arr)):
    if arr[i] > sec and arr[i] != high :
        sec = arr[i]

print(high,sec)
