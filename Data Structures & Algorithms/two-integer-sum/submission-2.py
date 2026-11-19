class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map = defaultdict(int)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in check_map:
                return [check_map[diff], i]
            check_map[n] = i
        