class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0

        for read in range(len(nums)):
            while write < 1 or nums[write - 1] != nums[read]:
                nums[write] = nums[read]
                write += 1
            
        return write