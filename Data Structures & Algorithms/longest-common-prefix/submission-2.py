class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        smallest_str = strs[0]

        for s in strs:
            if len(s) < len(smallest_str):
                smallest_str = s
        
        for i in range(len(smallest_str)):
            for s in strs:
                if smallest_str[i] != s[i]:
                    return smallest_str[:i]
        
        return smallest_str