class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        # converting list to n is O(n)
        nums_set = set(nums)
        
        max_seq_len = 0
        while nums_set:
            # pick out random sequence [mid - negative: mid: mid + positive] while removing it's elements from initial set
            seq_mid_n = nums_set.pop()

            positive_shift = 0
            while (seq_mid_n + positive_shift + 1) in nums_set:
                nums_set.remove(seq_mid_n + positive_shift + 1)
                positive_shift += 1
                
            negative_shift = 0
            while(seq_mid_n - negative_shift - 1) in nums_set:
                nums_set.remove(seq_mid_n - negative_shift - 1)
                negative_shift += 1
                
            seq_len = 1 + positive_shift + negative_shift
            if seq_len > max_seq_len:
                max_seq_len = seq_len
        return max_seq_len

s = Solution()
print("[0,3,7,2,5,8,4,6,0,1]", s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print("[100,4,200,1,3,2]", s.longestConsecutive([100,4,200,1,3,2]))
