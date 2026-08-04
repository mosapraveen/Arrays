def remove(arr):
    if not arr:
        return []
    
    i=0
    for j in range(1,len(arr)):
        Duplicate = False
        
        for k in range(i+1):
            if arr[k]==arr[j]:
                Duplicate = True
                break
        if not Duplicate :
            i+=1
            arr[i] = arr[j]  #remove the duplicates permnently
    arr = arr[:i+1]
    return arr

arr = list(map(int,input().split(" ")))
print(remove(arr))


'''
Input:
7 7 8 8 9 4 5 2 

Output:  
[7, 8, 9, 4, 5, 2]'''