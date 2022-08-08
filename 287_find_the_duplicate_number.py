LARGE_NUMBER = 1000000

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = nums[i] % LARGE_NUMBER
            if nums[idx] > LARGE_NUMBER:
                res = idx
                break
            else:
                nums[idx] += LARGE_NUMBER
        
        for i in range(len(nums)):
            nums[i] %= LARGE_NUMBER
        return res
