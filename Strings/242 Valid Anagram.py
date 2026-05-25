#description 
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 #Example 1:

#Input: s = "anagram", t = "nagaram"

#Output: true

def isAnagram(s, t):
        
        if len(s) != len(t):
            return False

        t_list = list(t)
        empty = []

        for i in s:
            if i in t_list:  
                empty.append(i)
                t_list.remove(i)

        return len(empty) == len(s)