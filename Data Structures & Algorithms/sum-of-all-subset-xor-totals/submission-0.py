class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Empty Subset with XOR 0
        # Get all subsets first

        result = 0

        def solve(index,current_subset):
            nonlocal result
            if index == len(nums):
                localresult = 0
                for num in current_subset:
                    localresult ^= num
                result += localresult
                return
            
            current_subset.append(nums[index])
            solve(index + 1, current_subset)
            current_subset.pop()
            solve(index + 1, current_subset)

        solve(0, [])
        return result