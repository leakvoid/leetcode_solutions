class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # solution in O(m + n)
        mid = (len(nums1) + len(nums2)) // 2 + 1
        
        prev = None
        cur = None
        i = 0
        j = 0
        k = 0
        while k < mid:
            if j == len(nums2) or i == len(nums1):
                break

            prev = cur
            if nums1[i] > nums2[j]:
                cur = nums2[j]
                j += 1
            else:
                cur = nums1[i]
                i += 1
            k += 1
        
        if i == len(nums1):
            while k < mid:
                prev = cur
                cur = nums2[j]
                j += 1
                k += 1
        elif j == len(nums2):
            while k < mid:
                prev = cur
                cur = nums1[i]
                i += 1
                k += 1
        
        if (len(nums1) + len(nums2)) % 2:
            return cur
        return (prev + cur) / 2
