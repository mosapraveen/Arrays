# You are given an integer array height of length n. There are n vertical lines drawn such that the
# two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the 
# container contains the most water.
# Return the maximum amount of water a container can store.

heights = list(map(int,input().split(" ")))

left = 0
right = len(heights)-1
res = 0
while left<=right:
    width = right - left
    height = min(heights[left] , heights[right])
    area = height * width
    res = max(res,area)
    
    if heights[left] < heights[right] :
        left+=1
    else:
        right -= 1
print(res)