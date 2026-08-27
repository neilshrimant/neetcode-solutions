class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        res = 0
        l = 0

        for r in range(len(s)):
            print(s[r], lookup)
            while s[r] in lookup:
                lookup.remove(s[l])
                l += 1
            lookup.add(s[r])
            res = max(res, r - l + 1)
        
        return res

        