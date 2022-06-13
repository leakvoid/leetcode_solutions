class Solution:
    def reverse_arr(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                j = len(nums) - 1
                while nums[j] <= nums[i - 1]:
                    j -= 1
                
                nums[j], nums[i-1] = nums[i-1], nums[j]
                k = i
                break
            
        self.reverse_arr(nums, k, len(nums) - 1)
