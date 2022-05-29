
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left_i = 0
        right_i = len(height) - 1
        
        max_left_h = height[left_i]
        max_right_h = height[right_i]
        max_area = min(max_left_h, max_right_h) * (right_i - left_i)
        
        while right_i - left_i > 0:
            if max_left_h < max_right_h:
                left_i += 1
                if height[left_i] > max_left_h:
                    max_left_h = height[left_i]
            else:
                right_i -= 1
                if height[right_i] > max_right_h:
                    max_right_h = height[right_i]
                
            area = min(max_left_h, max_right_h) * (right_i - left_i)
            if area > max_area:
                max_area = area
                
        return max_area

s = Solution()
print("[1,8,6,2,5,4,8,3,7]:", s.maxArea([1,8,6,2,5,4,8,3,7]))
