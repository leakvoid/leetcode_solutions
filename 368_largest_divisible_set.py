class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1] * len(nums)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    dp[j] = max(dp[j], dp[i] + 1)
        print(dp)
        
        i, n = dp.index(max(dp)), max(dp)
        res = [nums[i]]
        for k in range(i - 1, -1, -1):
            if res[-1] % nums[k] == 0 and dp[k] == n - 1:
                res.append(nums[k])
                n -= 1
        return res[::-1]
