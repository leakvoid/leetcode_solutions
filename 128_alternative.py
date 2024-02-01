class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for n in nums:
            if (n - 1) not in nums_set:
                cur_len = 1
                while (n + cur_len) in nums_set:
                    cur_len += 1
                max_len = max(cur_len, max_len)
        
        return max_len
