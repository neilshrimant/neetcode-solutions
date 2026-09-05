class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res, cur = [], []

        def kSum(k, start, target):
            if k == 2:
                l, r = start, n - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(cur + [nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                return
            
            for i in range(start, n - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                cur.pop()
        
        kSum(3, 0, 0)
        return res
