class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        state = 0
        l = 0
        res = float("inf")

        for r in range(len(nums)):
            state += nums[r]
            while state >= target:
                res = min(res, (r - l + 1))
                state -= nums[l]
                l += 1
            
        return res if res != float("inf") else 0
