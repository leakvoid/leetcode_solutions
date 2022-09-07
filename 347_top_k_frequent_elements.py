import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = {}
        for n in nums:
            if n not in nums_counter:
                nums_counter[n] = 1
            else:
                nums_counter[n] += 1
        
        nums_heap = []
        for n in nums_counter:
            heapq.heappush( nums_heap, (nums_counter[n], n) )
            if len(nums_heap) > k:
                heapq.heappop( nums_heap )
        
        res = []
        for i in range( len(nums_heap) ):
            n_pair = heapq.heappop( nums_heap )
            res.append( n_pair[1] )
        return res
