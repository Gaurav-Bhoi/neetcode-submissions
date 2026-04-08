class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
    
        if n < 1:
            return
        
        obj = defaultdict(list)
        
        for i in range(n):
            arr = [0] * 26
            for char in strs[i]:
                arr [ord(char) - ord("a")] += 1 
            
            obj[tuple(arr)].append(strs[i])
        
        return list(obj.values())