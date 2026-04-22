class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 1: return []
        
        zeroes = nums.count(0)
        if zeroes > 1:
            return [0 for num in nums]
        
        idx = None  
        if zeroes == 1:
            idx = nums.index(0)
        
        
        mul = 1
        for index in range(n):
            if idx != index:
                mul *= nums[index]  
        
        if idx is None:
            pass
        res = [mul//nums[index] if idx is None else 0 if idx != index else mul for index in range(n) ]
        return res