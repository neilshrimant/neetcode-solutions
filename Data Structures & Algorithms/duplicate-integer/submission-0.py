class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_map = {}

        for num in nums:
            if num in check_map:
                return True
            check_map[num] = check_map.get(num,0) + 1
        
        return False