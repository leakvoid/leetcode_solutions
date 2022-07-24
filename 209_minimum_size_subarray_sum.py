class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sm = 0
        res = len(nums) + 1
        for right in range(len(nums)):
            sm += nums[right]
            while target <= sm and left <= right:
                r = right - left + 1
                if r < res:
                    res = r
                sm -= nums[left]
                left += 1
                
        return 0 if res == len(nums) + 1 else res
