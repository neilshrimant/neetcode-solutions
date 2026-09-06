class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count_map = {}
        odd_count = 0
        for c in s:
            count_map[c] = 1 + count_map.get(c, 0)

        for key in count_map:
            if count_map[key] % 2 == 1:
                odd_count += 1

        if odd_count > 1:
            return False 
        else:
            return True

        