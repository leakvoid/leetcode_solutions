import math

class Solution:
    def find_smallest_idx(self, nums, start, end, first):
        if start == end:
            if first > nums[start]:
                return start
            else:
                return start + 1
        
        mid = (start + end) / 2
        mid_f = math.floor(mid)
        if first > nums[mid_f]:
            return self.find_smallest_idx(nums, start, mid_f, first)
        else:
            return self.find_smallest_idx(nums, math.ceil(mid), end, first)
    
    def find(self, nums, start, end, target):
        if start == end:
            if nums[start] == target:
                return start
            else:
                return -1
        
        mid = (start + end) / 2
        mid_c = math.ceil(mid)
        if target == nums[mid_c]:
            return mid_c
        elif target > nums[mid_c]:
            return self.find(nums, mid_c, end, target)
        else:
            return self.find(nums, start, math.floor(mid), target)
            
    
    def search(self, nums: List[int], target: int) -> int:
        shift = self.find_smallest_idx(nums, 0, len(nums) - 1, nums[0])
        if shift == len(nums):
            return self.find(nums, 0, len(nums) - 1, target)
        
        if target < nums[0]:
            return self.find(nums, shift, len(nums) - 1, target)
        else:
            return self.find(nums, 0, shift - 1, target)
