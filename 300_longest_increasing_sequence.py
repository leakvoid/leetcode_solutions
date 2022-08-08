class Solution:
    def binarySearch(self, start, end, target, res):
        if start == end:
            return start

        mid = (start + end) // 2

        if res[mid] == target:
            return mid
        elif res[mid] > target:
            return self.binarySearch(start, mid, target, res)
        return self.binarySearch(mid + 1, end, target, res)
    
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
                continue

            j = self.binarySearch(0, len(res) - 1, nums[i], res)
            res[j] = nums[i]

        return len(res)
