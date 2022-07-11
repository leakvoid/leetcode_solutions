class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        val = nums[0]
        start = 0
        count = 1
        for i in range(1, len(nums)):
            cur_val = nums[i]
            if val == cur_val:
                if count < 2:
                    nums[start + count] = cur_val
                    count += 1
            else:
                val = cur_val
                start += count
                nums[start] = val
                count = 1
        return start + count
