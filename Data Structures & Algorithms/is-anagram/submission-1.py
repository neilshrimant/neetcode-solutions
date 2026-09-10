class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        for key in count_s:
            if key not in count_t or count_s[key] != count_t[key]:
                return False
        
        return True

        # Time : O(n) -> n = len(s)
        # Space : O(n) -> n = len(s)