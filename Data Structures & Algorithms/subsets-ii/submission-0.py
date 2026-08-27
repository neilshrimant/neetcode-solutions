class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(i,comb):
            if i == len(nums):
                res.append(comb.copy())
                return
            comb.append(nums[i])
            helper(i + 1,comb)
            comb.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i + 1,comb)
        helper(0, [])
        return res


        