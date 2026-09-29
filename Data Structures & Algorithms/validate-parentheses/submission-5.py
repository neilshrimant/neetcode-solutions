class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        check_stack = []
        for c in s:
            if c in valid_map:
                if not check_stack or check_stack.pop() != valid_map[c]:
                    return False
            else:
                check_stack.append(c)
        
        return True if not check_stack else False