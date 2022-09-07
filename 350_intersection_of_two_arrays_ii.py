class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_d = {}
        for n in nums1:
            if n not in nums1_d:
                nums1_d[n] = 1
            else:
                nums1_d[n] += 1
        
        res = []
        for n in nums2:
            if n in nums1_d and nums1_d[n] > 0:
                nums1_d[n] -= 1
                res.append(n)
        return res
