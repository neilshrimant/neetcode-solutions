class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for n in nums:
            temp = max(prev + n, curr)
            prev = curr
            curr = temp
        return curr

        