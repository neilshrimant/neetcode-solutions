class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            length = 1
            while n + length in nums:
                length += 1
            res = max(res, length)
        
        return res
        