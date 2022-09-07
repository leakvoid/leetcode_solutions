class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_s = set(nums1)
        nums2_s = set(nums2)
        
        res = []
        for n in nums2_s:
            if n in nums1_s:
                res.append(n)
        return res
