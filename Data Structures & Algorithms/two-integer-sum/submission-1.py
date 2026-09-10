class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map = {}

        for i, n in enumerate(nums):
            remaining = target - nums[i]
            if remaining in check_map:
                return [check_map[remaining], i]
            check_map[n] = i
        
