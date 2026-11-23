class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0 : 1}
        res = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in sum_map:
                res += sum_map.get(curr_sum-k, 0)
            sum_map[curr_sum] = 1 + sum_map.get(curr_sum,0)
        
        return res