
class Solution:
    def find_rotation_point(self, nums, start, end, first):
        if start > end:
            return 0
        
        mid = start + (end - start) // 2
        if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
            return mid + 1
        
        if first == nums[mid]:
            for i in range(start, mid + 1):
                if nums[i] > first:
                    return self.find_rotation_point(nums, i, end, nums[i])
                elif nums[i] < first:
                    return i
        
        if first > nums[mid]:
            return self.find_rotation_point(nums, start, mid - 1, first)
        else:
            return self.find_rotation_point(nums, mid + 1, end, first)
        
    def find(self, nums, target, start, end, shift):
        if start > end:
            return False
        
        mid = start + (end - start) // 2
        s_mid = mid + shift
        if s_mid > len(nums) - 1:
            s_mid -= len(nums)

        if target == nums[s_mid]:
            return True
        if target < nums[s_mid]:
            return self.find(nums, target, start, mid - 1, shift)
        else:
            return self.find(nums, target, mid + 1, end, shift)
    
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            return nums[0] == target
        split = self.find_rotation_point(nums, 0, len(nums) - 1, nums[0])
        return self.find(nums, target, 0, len(nums) - 1, split)
        #return self.find(nums[split:] + nums[:split], target, 0, len(nums) - 1)
