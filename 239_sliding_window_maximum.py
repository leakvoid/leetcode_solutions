import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n_heap = []
        for i in range(k):
            heapq.heappush(n_heap, (-1 * nums[i], i))
        
        res = []
        res.append( -1 * n_heap[0][0] )
        
        start = 1
        end = k
        while end < len(nums):
            heapq.heappush(n_heap, (-1 * nums[end], end))
            
            while n_heap[0][1] < start:
                heapq.heappop(n_heap)
            
            res.append( -1 * n_heap[0][0] )
            start += 1
            end += 1
        return res
