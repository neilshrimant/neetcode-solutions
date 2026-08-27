class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        def helper(i, cap):
            if i == len(profit):
                return 0
            
            maxProfit = helper(i+1, cap)

            newCap = cap - weight[i]

            if newCap >= 0:
                p = profit[i] + helper(i+1, newCap)
                maxProfit = max(maxProfit, p)
            
            return maxProfit

        return helper(0, capacity)