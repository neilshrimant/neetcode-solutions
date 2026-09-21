class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur_sum = 0
        prefixSum = { 0 : 1 }

        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            res += prefixSum.get(diff, 0)
            prefixSum[cur_sum] = 1 + prefixSum.get(cur_sum, 0)
        
        return res
