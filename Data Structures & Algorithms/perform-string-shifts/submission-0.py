class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        net_effect = 0

        for direction, amount in shift:
            if direction == 0:
                net_effect -= amount
            else:
                net_effect += amount
        
        k = net_effect % len(s)

        return s[-k:] + s[:-k]
