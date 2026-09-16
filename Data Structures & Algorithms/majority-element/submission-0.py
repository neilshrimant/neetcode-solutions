class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}
        result = 0
        max_count = 0
        for n in nums:
            count_map[n] = 1 + count_map.get(n, 0)
        
        for k, v in count_map.items():
            if v > max_count:
                result = k
                max_count = v
        
        return result
