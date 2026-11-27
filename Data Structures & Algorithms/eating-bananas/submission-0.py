class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        def canEat(rate):
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p) / rate)
                if total_time > h:
                    return False
            return True if total_time <= h else False
        
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r - l) // 2
            if canEat(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
