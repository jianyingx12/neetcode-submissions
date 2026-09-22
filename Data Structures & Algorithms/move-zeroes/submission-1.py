class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ins = 0

        for x in range(len(nums)):
            if nums[x] != 0:
                nums[ins] = nums[x]
                ins += 1
                
        for x in range(ins, len(nums)):
            nums[x] = 0
        