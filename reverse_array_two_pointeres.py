# Reverseing array using two pointeres

n = int(input())
arr = list(map(int,input().split(" ")))

l,r = 0 , n-1

while l < r :
    arr[l] , arr[r] = arr[r] , arr[l]
    
    l+=1
    r-=1

print(arr)
