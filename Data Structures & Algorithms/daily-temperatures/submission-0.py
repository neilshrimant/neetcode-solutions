class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append((n, i))
        return res
        