class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) space(1)
        m = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if m == nums[i]:
                count += 1
            else:
                count -= 1
                
            if count == 0:
                m = nums[i]
                count = 1
        return m
        
    def majorityElement_simple(self, nums: List[int]) -> int:
        # simplest O(n ln n) space(1)
        mid = len(nums) // 2
        nums.sort()
        return nums[mid]
