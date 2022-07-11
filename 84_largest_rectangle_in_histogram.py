class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        stack = [[0,0]]
        max_area = 0
        for i in range(len(heights)):
            if stack[-1][0] < heights[i]:
                stack.append([heights[i], i])
            elif stack[-1][0] > heights[i]:
                while True:
                    last = stack.pop()
                    area = last[0] * (i - last[1])
                    if area > max_area:
                        max_area = area
                        
                    if stack[-1][0] == heights[i]:
                        break
                    if stack[-1][0] < heights[i]:
                        stack.append([heights[i], last[1]])
                        break
        
        for e in stack:
            area = e[0] * (i - e[1] + 1)
            if area > max_area:
                max_area = area
                    
        return max_area

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
