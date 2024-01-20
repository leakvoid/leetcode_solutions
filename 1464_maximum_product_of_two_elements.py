import heapq

class Solution:
    def maxProduct(self, nums) -> int:
        my_heap = []
        for n in nums:
            heapq.heappush(my_heap, n * (-1))

        largest = heapq.heappop(my_heap) * (-1)
        second_largest = heapq.heappop(my_heap) * (-1)
        return (largest - 1) * (second_largest - 1)