class Solution:
    def countElements(self, arr: List[int]) -> int:
        check_set = set()
        res = 0
        for num in arr:
            check_set.add(num)
        
        for num in arr:
            if num + 1 in check_set:
                res += 1

        return res
        