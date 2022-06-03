class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        shift = 0
        for i in range(len(nums)):
            if nums[i] == val:
                shift += 1
            else:
                nums[i - shift] = nums[i]
        return len(nums) - shift
