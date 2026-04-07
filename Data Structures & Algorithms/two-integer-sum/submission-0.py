class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        
        for index, item in enumerate(nums):
            pair_num = target - item

            if pair_num in obj:
                return [obj[pair_num], index ]
            else:
                obj[item] = index