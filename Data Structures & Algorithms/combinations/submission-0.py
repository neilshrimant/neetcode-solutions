class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def solve(num, current_comb):
            if len(current_comb) == k:
                result.append(current_comb.copy())
                return

            if num > n or len(current_comb) > k:
                return

            
            current_comb.append(num)
            solve(num+1, current_comb)
            current_comb.pop()
            solve(num+1, current_comb)
        
        solve(1, [])
        return result
        