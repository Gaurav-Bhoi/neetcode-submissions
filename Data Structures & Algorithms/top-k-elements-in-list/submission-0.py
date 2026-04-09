class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < 1: return

        counter_hashmap = Counter(nums)
        counter_max = counter_hashmap.most_common()
        res = []
        
        for item in counter_max:
            if len(res) == k:
                return res
            res.append(item[0])
        return res
