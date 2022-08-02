from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for i in range(k):
            while len(dq) > 0 and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
                
        res = []
        res.append(nums[dq[0]])
        
        start = 1
        end = k
        while end < len(nums):
            while len(dq) > 0 and dq[0] < start:
                dq.popleft()
                
            while len(dq) > 0 and nums[end] > nums[dq[-1]]:
                dq.pop()
            dq.append(end)
            
            res.append(nums[dq[0]])
                
            start += 1
            end += 1
        return res
