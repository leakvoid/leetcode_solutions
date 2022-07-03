class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) == 1:
            return True
        
        last_idx = len(nums) - 1
        max_reach_idx = jump_pos_idx = 0
        max_reach = jump_length = nums[0]

        while jump_length != 0:
            if max_reach >= last_idx:
                return True
            
            for i in range(1, jump_length + 1):
                cur_reach_idx = jump_pos_idx + i
                cur_reach = cur_reach_idx + nums[cur_reach_idx]
                if cur_reach >= max_reach:
                    max_reach_idx = cur_reach_idx
                    max_reach = cur_reach

            jump_pos_idx = max_reach_idx
            jump_length = nums[jump_pos_idx]

        return False

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))
print(s.canJump([2,0]))
