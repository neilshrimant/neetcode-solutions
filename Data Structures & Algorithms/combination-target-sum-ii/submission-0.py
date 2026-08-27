class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def helper(i, comb, total):
            if i == len(candidates):
                if total == target:
                    res.append(comb.copy())
                    return
                else:
                    return
            comb.append(candidates[i])
            helper(i + 1, comb, total + candidates[i])
            comb.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, comb, total)
        helper(0, [], 0)
        return res

        