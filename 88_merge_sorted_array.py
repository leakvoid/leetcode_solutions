class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        insert_point = m + n - 1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[insert_point] = nums1[i]
                i -= 1
            else:
                nums1[insert_point] = nums2[j]
                j -= 1
            insert_point -= 1
            
        while j >= 0:
            nums1[insert_point] = nums2[j]
            j -= 1
            insert_point -= 1

s = Solution()
res = [1,2,3,0,0,0]
s.merge(res, 3, [2,5,6], 3)
print(res)
