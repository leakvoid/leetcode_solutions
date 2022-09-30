class Solution:
    def counting_sort(self, arr, exp1):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)
        
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]
        
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
    
    def radix_sort(self, arr):
        max1 = max(arr)
        
        exp = 1
        while max1 / exp >= 1:
            self.counting_sort(arr, exp)
            exp *= 10
    
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        self.radix_sort(nums)
        max_distance = 0
        for i in range(1, len(nums)):
            distance = nums[i] - nums[i - 1]
            if distance > max_distance:
                max_distance = distance
        
        return max_distance
