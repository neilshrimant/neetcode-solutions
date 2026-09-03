class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        check_map = {}
        for n in nums:
            check_map[n] = 1 + check_map.get(n, 0)

        highest = -1
        for n in nums:
            if n > highest:
                if check_map[n] > 1:
                    continue
                else:
                    highest = n
        return highest


