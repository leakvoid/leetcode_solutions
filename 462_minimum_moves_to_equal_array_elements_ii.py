class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        mid = len(nums) // 2
        if len(nums) % 2:
            median = nums[mid]
        else:
            median = (nums[mid - 1] + nums[mid]) // 2

        res = 0
        for n in nums:
            res += abs(n - median)
        return res
