#description
#Given a string s, find the first 
# non-repeating character in it and 
# return its index. If it does not exist, return -1.

 #Example 1:

#Input: s = "leetcode"
#Output: 0
#Explanation:
#The character 'l' at index 0 is the first character
#  that does not occur at any other index.

def firstUniqChar(s):
        
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
                
        return -1