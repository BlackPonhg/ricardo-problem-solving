from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        for x in nums:
            if x != 0:
                nums[write] = x
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0
            