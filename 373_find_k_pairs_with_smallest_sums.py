import heapq

class Solution:
    def add_unique_pair(self, n1_i, n2_i):
        if n1_i not in self.used_pairs:
            self.used_pairs[n1_i] = set()
        self.used_pairs[n1_i].add(n2_i)
    
    def not_added(self, n1_i, n2_i):
        if n1_i not in self.used_pairs:
            return True
        if n2_i not in self.used_pairs[n1_i]:
            return True
        return False
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k = min(len(nums1) * len(nums2), k)
        
        res = [ [nums1[0], nums2[0]] ]
        res_size = 1
        
        sum_heap = []
        if len(nums1) > 1:
            heapq.heappush( sum_heap, (nums1[1] + nums2[0], (1, 0)) )
        if len(nums2) > 1:
            heapq.heappush( sum_heap, (nums1[0] + nums2[1], (0, 1)) )
        
        self.used_pairs = {}
        self.add_unique_pair(0, 0)
        
        while res_size < k:
            next_smallest = heapq.heappop(sum_heap)
            
            res_size += 1
            n1_i = next_smallest[1][0]
            n2_i = next_smallest[1][1]
            res.append( [nums1[n1_i], nums2[n2_i]] )
            
            if n1_i + 1 < len(nums1) and self.not_added(n1_i + 1, n2_i):
                self.add_unique_pair(n1_i + 1, n2_i)
                heapq.heappush( sum_heap, (nums1[n1_i + 1] + nums2[n2_i], (n1_i + 1, n2_i)) )
            if n2_i + 1 < len(nums2) and self.not_added(n1_i, n2_i + 1):
                self.add_unique_pair(n1_i, n2_i + 1)
                heapq.heappush( sum_heap, (nums1[n1_i] + nums2[n2_i + 1], (n1_i, n2_i + 1)) )
        
        return res
