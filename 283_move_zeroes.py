class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_count = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                z_count += 1
                break
            j += 1
        
        for i in range(j + 1, len(nums)):
            if nums[i] == 0:
                z_count += 1
            else:
                nums[i - z_count] = nums[i]
                
        for i in range(len(nums) - z_count, len(nums)):
            nums[i] = 0
