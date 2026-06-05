#description
#iven a pattern and a string s, find if s follows the same pattern.

#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

#Each letter in pattern maps to exactly one unique word in s.
#Each unique word in s maps to exactly one letter in pattern.
#No two letters map to the same word, and no two words map to the same letter.
 
#Example 1:
#Input: pattern = "abba", s = "dog cat cat dog"
#Output: true

def wordPattern(pattern, s):

        
        words = s.split()
        
        
        if len(pattern) != len(words):
            return False
        
        
        mapping = {}
        
        for char, word in zip(pattern, words):
            
            if char in mapping:
                if mapping[char] != word:
                    return False
            
            else:
                if word in mapping.values():
                    return False
                mapping[char] = word
                
        return True