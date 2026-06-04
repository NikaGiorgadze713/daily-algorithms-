#definiton Given two strings ransomNote and magazine, return true if 
# ransomNote can be constructed by using the letters from magazine and false otherwise.

#Each letter in magazine can only be used once in ransomNote.

 

#Example 1:

#Input: ransomNote = "a", magazine = "b"
#Output: false
#Example 2:

#Input: ransomNote = "aa", magazine = "ab"
#Output: false



def canConstruct( ransomNote, magazine):
        
        
        char_count = {}
        a = list(ransomNote)
        for char in magazine:
            if char in char_count:
                char_count[char] += 1  
            else:
                char_count[char] = 1

        for char in ransomNote:
    
            if char not in char_count or char_count[char] <= 0:
                return False
    
    
            char_count[char] -= 1

        return True