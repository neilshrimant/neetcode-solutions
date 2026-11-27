class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = float("inf")

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap
                currCap -= w
            return True
        
        l, r = max(weights), sum(weights)
        while l <= r:
            m = l + (r - l) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
