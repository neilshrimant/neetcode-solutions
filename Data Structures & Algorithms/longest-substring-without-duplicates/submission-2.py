class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_map = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            
            while freq_map[s[r]] > 1:
                freq_map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res