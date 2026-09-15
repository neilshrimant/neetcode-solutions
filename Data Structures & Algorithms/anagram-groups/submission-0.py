class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        result = []

        check_map = defaultdict(list)

        for s in strs:
            check_map[''.join(sorted(s))].append(s)

        return list(check_map.values())

        