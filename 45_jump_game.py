class Solution:
    def jump(self, nums: [int]) -> int:
        last_idx = len(nums) - 1
        cur_idx = 0
        
        jumps = 0
        while cur_idx < last_idx:
            jumps += 1
            cur_max_jump = nums[cur_idx]
            
            max_reach_weight = 0
            max_reach_idx = 0
            for l in range(1, cur_max_jump + 1):
                reach_idx = cur_idx + l
                reach_weight = reach_idx + nums[reach_idx]
                if reach_idx >= last_idx:
                    return jumps
                
                if reach_weight > max_reach_weight:
                    max_reach_idx = reach_idx
                    max_reach_weight = reach_weight
            cur_idx = max_reach_idx
        return jumps

s = Solution()
print("[2,3,1,1,4]:", s.jump([2,3,1,1,4]))
print("[2,3,0,1,4]:", s.jump([2,3,0,1,4]))
