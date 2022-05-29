import math

class Solution(object):
    
    def get_median(self, arr, left, right):
        i1 = int(left + math.floor((right - left) / 2.0))
        i2 = int(left + math.ceil((right - left) / 2.0))
        #print("arr:(", arr[left], arr[right], ")mid:(", arr[i1], arr[i2], ")")
        return ((arr[i1] + arr[i2]) / 2.0, i1, i2)
    
    def solve(self, r1, r2):        
        l_shift = 0
        r_shift = 0
        
        r1_l = 0
        r1_r = len(r1) - 1
        r2_l = 0
        r2_r = len(r2) - 1

        if len(r1) == 0 and len(r2) == 0:
            return 0
        if len(r1) == 0:
            (res,i1,i2) = self.get_median(r2, r2_l, r2_r)
            return res
        if len(r2) == 0:
            (res,i1,i2) = self.get_median(r1, r1_l, r1_r)
            return res
        
        target = float(len(r1) + len(r2) - 1) / 2.0
        
        while True:
            r1_size = r1_r - r1_l + 1
            (r1_median, r1_i1, r1_i2) = self.get_median(r1, r1_l, r1_r)
            r2_size = r2_r - r2_l + 1
            (r2_median, r2_i1, r2_i2) = self.get_median(r2, r2_l, r2_r)
            if r1_median > r2_median:
                if r1_size > 3:
                    r_shift += r1_r - r1_i2
                    r1_r = r1_i2
                if r2_size > 3:
                    l_shift += r2_i1 - r2_l
                    r2_l = r2_i1
            else:
                if r1_size > 3:
                    l_shift += r1_i1 - r1_l
                    r1_l = r1_i1
                if r2_size > 3:
                    r_shift += r2_r - r2_i2
                    r2_r = r2_i2
            if r1_size <= 3 and r2_size <= 3:
                break

        res_sub = []
        i = 0
        j = 0
        while i < r1_size and j < r2_size:
            if r1[r1_l + i] < r2[r2_l + j]:
                res_sub.append(r1[r1_l + i])
                i += 1
            else:
                res_sub.append(r2[r2_l + j])
                j += 1
        if r1_l == r1_r:
            r1_end = r1_r + 1
            r2_end = r2_r + 2
        elif r2_l == r2_r:
            r1_end = r1_r + 2
            r2_end = r2_r + 1
        else:
            r1_end = r1_r + 1
            r2_end = r2_r + 1
        res_sub = res_sub + r1[(r1_l + i):r1_end] + r2[(r2_l + j):r2_end]

        target = target - l_shift
        target_l = int(math.floor(target))
        target_r = int(math.ceil(target)) 
        print("\ntarget_l:", target_l)
        print("target_r:", target_r)
        print("r1:", r1[r1_l], r1[r1_r])
        print("r2:", r2[r2_l], r2[r2_r])
        print("res_sub:", res_sub)
        print("l_shift:", l_shift)
        print("r_shift:", r_shift)
        print("result:", res_sub[target_l], res_sub[target_r])
        return float(res_sub[target_l] + res_sub[target_r]) / 2.0
                   
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        return self.solve(nums1, nums2)

s = Solution()
print("solution for [10, 20, (22, 30), 33, 40]:", s.findMedianSortedArrays([10,20,30,40], [22,33])) # [10, 20, (22, 30), 33, 40]
print("solution for [1, 2, 10, (20, 22), 30, 33, 40]:", s.findMedianSortedArrays([10,20,30,40], [1,2,22,33])) # [1, 2, 10, (20, 22), 30, 33, 40]
print("solution for [1, 2, 10, 20, (22), 30, 33, 40, 44]:", s.findMedianSortedArrays([10,20,30,40], [1,2,22,33,44])) # [1, 2, 10, 20, (22), 30, 33, 40, 44]
print("solution for [5, 10, (20), 30, 40]:", s.findMedianSortedArrays([10,20,30,40], [5])) # [5, 10, (20), 30, 40]
print("solution for [5, 10, (20), 30, 40]:", s.findMedianSortedArrays([5], [10,20,30,40])) # [5, 10, (20), 30, 40]
print("solution for [1,2,7,8,9,(50),100,101,110,200,300]:", s.findMedianSortedArrays([1,2,8,9], [7,50,100,101,110,200,300])) # [1,2,7,8,9,(50),100,101,110,200,300]
print("solution for [1, (2, 3), 4]:", s.findMedianSortedArrays([1, 2], [3, 4])) # [1, (2, 3), 4]
print("solution for [1, (2, 3), 4]:", s.findMedianSortedArrays([3, 4], [1, 2])) # [1, (2, 3), 4]
print("solution for [(1)]:", s.findMedianSortedArrays([],[1]))
print("solution for [(2, 3)]:", s.findMedianSortedArrays([],[2,3]))
print("solution for [(2, 3)]:", s.findMedianSortedArrays([2,3],[]))
print("solution for [1][2,3,4,5,6]:", s.findMedianSortedArrays([1],[2,3,4,5,6]))
print("solution for [5],[1,2,3,4,6]:", s.findMedianSortedArrays([5],[1,2,3,4,6]))
print("solution for [1,5],[2,3,4,6]:", s.findMedianSortedArrays([1,5],[2,3,4,6]))
print("solution for [6],[1,2,3,4,5,7,8] [1,2,3,(4,5),6,7,8]:", s.findMedianSortedArrays([6],[1,2,3,4,5,7,8]))
# [6] [4, 5, 7, 8]
print("solution for [6],[1,2,3,4,5,7,8] [1,2,3,(4,5),6,7,8]:", s.findMedianSortedArrays([1,2,3,4,5,7,8],[6]))
