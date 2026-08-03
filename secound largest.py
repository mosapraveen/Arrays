import sys

n=int(input())
arr = list(map(int,input().split(",")))


high = -sys.maxsize-1
sec = -sys.maxsize-1

for i in range(len(arr)):
    if arr[i] > high :
        high = arr[i]
        
for i in range(len(arr)):
    if arr[i] > sec and arr[i] != high :
        sec = arr[i]

print(high,sec)
