n=int(input())
arr = list(map(int,input().split(",")))

key = int(input())

for i in range(len(arr)):
    if arr[i] == key :
        print(f"key found at `{i}` : ")
        break
else:
    print("key not found")
