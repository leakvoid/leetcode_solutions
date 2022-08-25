import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_counter = {}
        
        for n in arr:
            if n not in arr_counter:
                arr_counter[n] = 1
            else:
                arr_counter[n] += 1
        
        heap = []
        for key in arr_counter:
            heapq.heappush(heap, arr_counter[key] * (-1))
        
        half_size = len(arr) // 2
        counter = 0
        total_sum = 0
        while True:
            counter += 1
            total_sum += (-1) * heapq.heappop(heap)
            if total_sum >= half_size:
                return counter
