class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj = {}

        for item in nums:
            if item in obj:
                return True
            
            obj[item] = 1
        
        return False