class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            print("Cusum is :" + str(curSum))
            maxSum = max(maxSum, curSum)
            print("Maxsum is :" + str(maxSum))
        return maxSum

        