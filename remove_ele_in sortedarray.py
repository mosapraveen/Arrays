n = int(input())
arr = list(map(int,input().split(" ")))

d = []

for i in arr :
    if i not in d:
        d.append(i)
print(d)
