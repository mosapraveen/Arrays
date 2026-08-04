arr = list(map(int,input().split()))
val= int(input())

i=0
for j in range(0,len(arr)):
    if val != arr[j] :
        arr[i] = arr[j]
        i+=1
arr=arr[:i+1]
print(arr)

'''
Input:
    7 7 8 8 9 4 5 2
    8
Output:
    [7, 7, 9, 4, 5, 2, 5]
'''