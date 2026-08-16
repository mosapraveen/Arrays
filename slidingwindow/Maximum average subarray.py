# Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value 
# and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# nums = list(map(int,input("enter elements in array : ").split(" ")))
# k = int(input("enter the k value : "))
# current_avg = sum(nums[:k])/ k
# max_avg = current_avg
# if k > len(nums):
#     print(f"you must enter more elemnts then {k}")
# else:
#     for i in range(k,len(nums)):
#         # find new average 
#         current = ((k*current_avg) - nums[i-k]) 
#         current_avg = (current + nums[i]) / k
#         if current_avg > max_avg :
#             max_avg = current_avg
# print(max_avg)


#  another way
#  same logic but here we find large subarray sum and then we make avg with diffrent way
# becaue above solution is not working in leetcode

nums = list(map(int,input("enter elements in array : ").split(" ")))
k = int(input("enter the k value : "))

current = sum(nums[:k])
maxsum =current
for i in range(k,len(nums)):
    current = current - nums[i-k] + nums[i]
    if maxsum < current :
        maxsum = current
print(maxsum/k)