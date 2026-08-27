class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        cache = [[-1] * (M+1) for _ in range(N)]

        def helper(i, cap, cache):
            if i == len(profit):
                return 0
            if cache[i][cap] != -1:
                return cache[i][cap]
            
            cache[i][cap] = helper(i+1, cap, cache)

            newCap = cap - weight[i]

            if newCap >= 0:
                p = profit[i] + helper(i+1, newCap, cache)
            
                cache[i][cap] = max(cache[i][cap], p)

            return cache[i][cap]
        
        return helper(0, capacity, cache)
            
