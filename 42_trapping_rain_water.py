class Solution:
    def trap(self, height: [int]) -> int:
        total_water = 0
        
        # left_highest_wall
        lhw_idx = 0
        lhw_depth = height[lhw_idx]
        for i in range(1, len(height) - 1):
            cur_depth = height[i]
            if cur_depth >= lhw_depth:
                lhw_idx = i
                lhw_depth = cur_depth
            else:
                total_water += lhw_depth - cur_depth
                
        # right_highest_wall
        rhw_idx = len(height) - 1
        rhw_depth = height[rhw_idx]
        
        if rhw_idx <= lhw_idx or rhw_depth >= lhw_depth:
            return total_water
        
        # drain rightmost pool
        for i in range(rhw_idx - 1, lhw_idx - 1, -1):
            cur_depth = height[i]
            
            total_water -= lhw_depth - cur_depth
            if cur_depth >= rhw_depth:
                rhw_idx = i
                rhw_depth = cur_depth
            else:
                total_water += rhw_depth - cur_depth
                
        return total_water

s = Solution()
print("[0,5,1,0,4,4,2,1,0,1,3,2,1,2,1]:", s.trap([0,5,1,0,4,4,2,1,0,1,3,2,1,2,1]))
print("[0,1,0,2,1,0,1,3,2,1,2,1]:", s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print("[4,2,0,3,2,5]:", s.trap([4,2,0,3,2,5]))
