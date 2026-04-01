class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        obj1 = {}
        obj2 = {}
        
        for letter in s:
            if letter not in obj1:
                obj1[letter] = 1
            else:
                obj1[letter] = obj1[letter]+1
                
        for letter in t:
            if letter not in obj2:
                obj2[letter] = 1
            else:
                obj2[letter] = obj2[letter]+1
                
        
        return obj1 == obj2
        