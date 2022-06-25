# need to reflect some more
# it uses space O(1) because it completely wrecks input array and does wierd in place manipulations
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
                
        shift = n + 69
        for i in range(n):
            val = nums[i] % shift
            if val != 0:
                nums[val - 1] += shift
          
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        
        return n + 1

s = Solution()
print(s.firstMissingPositive([9,10,4,7,3,8,1,-2,2,5,11,11,11,11]))
