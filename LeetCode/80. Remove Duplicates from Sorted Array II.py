class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3: return len(nums)

        write_pointer = read_pointer = 2
        while read_pointer < len(nums):
            if nums[read_pointer] != nums[write_pointer-2]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1
            read_pointer += 1
        return write_pointer
