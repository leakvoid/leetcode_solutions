import math

class Solution:
    def rec_search(self, nums, target, start, end):
        if end == start:
            if target > nums[start]:
                return end + 1
            else:
                return end
        
        mid = (start + end) / 2
        mid_c = math.ceil(mid)
        if nums[mid_c] == target:
            return mid_c
        elif target > nums[mid_c]:
            return self.rec_search(nums, target, mid_c, end)
        else:
            return self.rec_search(nums, target, start, math.floor(math.floor(mid)))
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.rec_search(nums, target, 0, len(nums) - 1)
