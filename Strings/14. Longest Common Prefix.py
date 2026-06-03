#description
#Write a function to find the longest common prefix string
#  amongst an array of strings.

#If there is no common prefix, return an empty string "".

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"

def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        
        empty = strs[0]
        matching = []
        
        
        for i in range(len(empty)):
            
            for k in range(1, len(strs)):
                
                
                if i >= len(strs[k]) or empty[i] != strs[k][i]:
                    
                    return "".join(matching)
            
            
            matching.append(empty[i])
            
        
        return "".join(matching)