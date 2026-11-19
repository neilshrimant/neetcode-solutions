class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = defaultdict(list)
        result = []

        for s in strs:
            group_map["".join(sorted(s))].append(s)
        
        for key in group_map:
            result.append(group_map[key])
        
        return result