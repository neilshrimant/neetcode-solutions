class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_sum = 0
        for ch in operations:
            if ch == "+":
                total_sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif ch == "D":
                total_sum += (2 * stack[-1])
                stack.append(stack[-1] * 2)
            elif ch == "C":
                total_sum -= stack.pop()
            else:
                total_sum += int(ch)
                stack.append(int(ch))

        return total_sum 
