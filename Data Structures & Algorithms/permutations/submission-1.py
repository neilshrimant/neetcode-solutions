class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def solve(perm, nums, pick):
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    solve(perm, nums, pick)
                    perm.pop()
                    pick[i] = False

        solve([], nums, [False] * len(nums))
        return result