class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26
        
        for index in range(len(s)):
            arr[ord(s[index]) - ord("a")]+=1 
            arr[ord(t[index]) - ord("a")]-=1 
            
        return not any(arr)
        