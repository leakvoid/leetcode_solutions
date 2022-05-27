
class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        r_hash = {}
        for i in range(len(nums)):
            sn = nums[i]
            fn = target - sn
            if fn in r_hash:
                return [r_hash[fn], i]
            r_hash[sn] = i

s = Solution()
print(s.twoSum([3,2,4], 6))
print(s.twoSum([2,5,5,11], 10))
print(s.twoSum([2,7,11,5], 9))
