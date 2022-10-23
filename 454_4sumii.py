class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        targets = {}
        for n1 in nums1:
            for n2 in nums2:
                n = n1 + n2
                if n in targets:
                    targets[n] += 1
                else:
                    targets[n] = 1
        
        res = 0
        for n3 in nums3:
            for n4 in nums4:
                n = (-1) * (n3 + n4)
                if n in targets:
                    res += targets[n]
        
        return res
