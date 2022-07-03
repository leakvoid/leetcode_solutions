import math

class Solution:
    def find_bound_rec(self, intervals, target, start, end):
        mid_f = math.floor((start + end) / 2)
        
        if target >= intervals[mid_f][0]:
            if mid_f + 1 == len(intervals) or target < intervals[mid_f + 1][0]:
                return mid_f
        
        if target < intervals[mid_f][0]:
            return self.find_bound_rec(intervals, target, start, mid_f)
        else:
            mid_c = math.ceil((start + end) / 2)
            return self.find_bound_rec(intervals, target, mid_c, end)
    
    def insert(self, intervals: [[int]], new_interval: [int]) -> [[int]]:
        aug_interval = [-1, -1]
        last = len(intervals) - 1
        
        if len(intervals) == 0:
            intervals.append(new_interval)
            return intervals
        
        if new_interval[0] < intervals[0][0]:
            left_bound = insert_pos = 0
            aug_interval[0] = new_interval[0]
        else:
            left_bound = self.find_bound_rec(intervals, new_interval[0], 0, last)
            if new_interval[0] <= intervals[left_bound][1]:
                insert_pos = left_bound
                aug_interval[0] = intervals[left_bound][0]
            else:
                insert_pos = left_bound + 1
                aug_interval[0] = new_interval[0]
                
        if new_interval[1] < intervals[0][0]:
            aug_interval[1] = new_interval[1]
            right_bound = 0
        else:
            right_bound = self.find_bound_rec(intervals, new_interval[1], left_bound, last)
            if new_interval[1] <= intervals[right_bound][1]:
                aug_interval[1] = intervals[right_bound][1]
            else:
                aug_interval[1] = new_interval[1]
            right_bound += 1
        
        del intervals[insert_pos:right_bound]
        intervals.insert(insert_pos, aug_interval)
        
        return intervals

s = Solution()
print("[[1,2],[3,5],[6,7],[8,10],[12,16]] insert [4,8]:", s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
