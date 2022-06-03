class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        reps = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev:
                reps += 1
            else:
                prev = nums[i]
                unique += 1
            nums[i - reps] = nums[i]
            
        return unique
