class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_set = set()

        for n in nums:
            if n in check_set:
                return True
            check_set.add(n)
        
        return False