class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _map = {}

        res = []

        for i, n in enumerate(nums2):
            _map[n] = i
        
        for n in nums1:
            res.append(_map[n])
        
        return res
