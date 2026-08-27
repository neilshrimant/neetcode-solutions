class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float("-inf")
        l , r = 0 , len(heights) - 1
        while l < r:
            if heights[l] < heights[r]:
                res = max(res, (r - l) * heights[l])
                l += 1
            else:
                res = max(res, (r - l) * heights[r])
                r -= 1
        return res

        