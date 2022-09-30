class Solution:
    def find_target(self, nums1, nums2, target):
        k = 0
        i = 0
        j = 0
        while k < target:
            if i == len(nums1) or j == len(nums2):
                break
            
            shift = max((target - k) // 2, 1)
            t_i = min(i - 1 + shift, len(nums1) - 1)
            t_j = min(j - 1 + shift, len(nums2) - 1)
            if nums1[t_i] < nums2[t_j]:
                i = t_i + 1
            else:
                j = t_j + 1
            k = i + j
        
        if i == len(nums1):
            if k < target:
                j = target - i
                return nums2[j - 1]
        if j == len(nums2):
            if k < target:
                i = target - j
                return nums1[i - 1]
        if i == 0:
            return nums2[j - 1]
        if j == 0:
            return nums1[i - 1]
        return max(nums1[i - 1], nums2[j - 1])
    
    # solution is O(log(m + n)); calling for find_target twice is a bit inefficient, can be done with one call with complex exit condition
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        target = (len(nums1) + len(nums2)) // 2 + 1
        
        if (len(nums1) + len(nums2)) % 2:
            return self.find_target(nums1, nums2, target)
        return (self.find_target(nums1, nums2, target) + self.find_target(nums1, nums2, target - 1)) / 2
