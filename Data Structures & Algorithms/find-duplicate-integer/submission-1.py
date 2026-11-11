# Constraints: Elements will be in range [1, n]. One repeated.
# Without modifying the array and without using extra space.

# Candidate: Every element in array.

# Search Space: Iterate over array.

# Condition: Element matches some other element in array

# Result: Element

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1

        for key in freq_map:
            if freq_map[key] > 1:
                return key

        return 0