import numpy as np

class Solution(object):

    def add_unique_node(self, res_tree, r):
        if r[0] in res_tree:
            second_branch = res_tree[r[0]]
            if r[1] not in second_branch:
                second_branch[r[1]] = r[2]
        else:
            res_tree[r[0]] = {r[1]:r[2]}
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3:
            return []

        unique_reps = {}
        for n in nums:
            if n in unique_reps:
                unique_reps[n] += 1
            else:
                unique_reps[n] = 1
        
        res_tree = {}
        
        first_used_nums = set()
        for i in range(len(nums) - 1):
            first_number = nums[i]
            if first_number in first_used_nums:
                continue
            else:
                first_used_nums.add(first_number)
            
            for j in range(i + 1, len(nums)):
                third_number = nums[j]
                second_number = -1 * (first_number + third_number)
                
                if second_number in unique_reps:
                    rep_count = 1
                    if first_number == second_number:
                        rep_count += 1
                    if third_number == second_number:
                        rep_count += 1
                    if rep_count > unique_reps[second_number]:
                        continue
                    
                    self.add_unique_node(res_tree, np.sort([first_number, second_number, third_number]))

        res = []
        for n0 in res_tree:
            second_level = res_tree[n0]
            for n1 in second_level:
                n2 = second_level[n1]
                res.append([n0,n1,n2])
        
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))

# import numpy as np

# class Solution(object):
    
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
        
#         if len(nums) < 3:
#             return []
                
#         res = []
#         used_nums = set()
#         added_arrays = set()
#         for i in range(len(nums) - 1):
#             first_number = nums[i]
#             if first_number in used_nums:
#                 continue
#             else:
#                 used_nums.add(first_number)
            
#             existing_nums = set()
#             for j in range(i + 1, len(nums)):
#                 third_number = nums[j]
                
#                 second_number = -1 * (first_number + third_number)
#                 if second_number in existing_nums:
#                     r = np.sort([first_number, second_number, third_number])
#                     str_r = str(r)
#                     if str_r not in added_arrays:
#                         res.append(r)
#                         added_arrays.add(str_r)
                        
#                 if third_number not in existing_nums:
#                     existing_nums.add(third_number)
        
#         return res
