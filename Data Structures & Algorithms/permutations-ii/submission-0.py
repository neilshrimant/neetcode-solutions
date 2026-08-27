class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() # Sort to handle duplicates

        def solve(index):
            # Base Case: A full permutation is formed.
            if index == len(nums):
                result.append(nums.copy())
                return

            # Use a set to track numbers used at the current level of recursion
            # to avoid starting new permutations with the same number.
            used_at_this_level = set()
            
            # Loop to choose which number to place at the 'index' position.
            for j in range(index, len(nums)):
                # If we've already placed this number at this position, skip.
                if nums[j] in used_at_this_level:
                    continue
                
                used_at_this_level.add(nums[j])

                # --- The Correct Backtracking Cycle ---
                
                # 1. Choose: Swap the number into the current position.
                nums[index], nums[j] = nums[j], nums[index]
                
                # 2. Explore: Recurse for the rest of the array.
                solve(index + 1)
                
                # 3. Un-choose: Swap it back to restore the state for the next loop iteration.
                nums[index], nums[j] = nums[j], nums[index]

        solve(0)
        return result