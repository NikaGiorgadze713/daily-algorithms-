#description
#A phrase is a palindrome if, after converting all
#  uppercase letters into lowercase letters and removing
#  all non-alphanumeric characters, it reads the same fo
# rward and backward. Alphanumeric characters include letters and 
# numbers.

#Given a string s, return true if it is a 
# palindrome, or false otherwise.

 

#Example 1:

#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.


def isPalindrome(s):
        
        clean_s = [c.lower() for c in s if c.isalnum()]
        return clean_s == clean_s[::-1]