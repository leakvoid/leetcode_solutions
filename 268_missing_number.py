class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(0)
        LARGE_NUM = 100000
        for i in range(len(nums) - 1):
            idx = nums[i] % LARGE_NUM
            nums[idx] += LARGE_NUM
            
        for i in range(len(nums)):
            if nums[i] < LARGE_NUM:
                return i
