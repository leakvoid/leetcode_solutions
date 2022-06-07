import math

class Solution:
    def rec_search(self, nums, target, start, end):
        if end == start:
            if target == nums[start]:
                return start
            else:
                return -1
        
        mid = (start + end) / 2
        mid_c = math.ceil(mid)
        if target == nums[mid_c]:
            return mid_c
        elif target > nums[mid_c]:
            return self.rec_search(nums, target, mid_c, end)
        else:
            return self.rec_search(nums, target, start, math.floor(math.floor(mid)))
        
    def find_left_bound(self, nums, target, start, end):
        if end == start:
            if target == nums[start]:
                return start
            else:
                return start + 1
            
        mid = (start + end) / 2
        mid_f = math.floor(mid)
        if target == nums[mid_f]:
            return self.find_left_bound(nums, target, start, mid_f)
        else:
            return self.find_left_bound(nums, target, math.ceil(mid), end)
        
    def find_right_bound(self, nums, target, start, end):
        if end == start:
            if target == nums[start]:
                return start
            else:
                return start - 1
            
        mid = (start + end) / 2
        mid_c = math.ceil(mid)
        if target == nums[mid_c]:
            return self.find_right_bound(nums, target, mid_c, end)
        else:
            return self.find_right_bound(nums, target, start, math.floor(mid))
    
    def searchRange(self, nums, target: int):
        if not nums:
            return [-1, -1]
        
        res = self.rec_search(nums, target, 0, len(nums) - 1)
        if res == -1:
            return [-1, -1]
        
        print("res", res)
        s = self.find_left_bound(nums, target, 0, res)
        e = self.find_right_bound(nums, target, res, len(nums) - 1)
        return [s, e]

s = Solution()
print("[0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4:", s.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10], 4))
