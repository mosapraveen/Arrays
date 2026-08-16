# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

s = input("enter the string : ")

sets = set()

left = 0 # pointer for sliding window

maxlength = 0 # string max length

for right in range(len(s)):
    
    # if duplicate exist , move the sliding window until we lost that element
    while s[right] in sets:
        sets.remove(s[left])
        left += 1
    
    # add the present element in the set
    sets.add(s[right])
    maxlength = max(maxlength , len(sets))
print(maxlength)




    