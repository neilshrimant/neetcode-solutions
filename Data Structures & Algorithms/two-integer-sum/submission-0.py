class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkMap = {}
        for i, n in enumerate(nums):
            if target - n in checkMap:
                return [checkMap[target - n], i]
            checkMap[n] = i