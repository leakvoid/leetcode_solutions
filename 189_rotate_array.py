class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
        
    def rotate_with_copy():
        k = k % len(nums)
        r = len(nums) - k
        rotated = nums[r:] + nums[:r]
        for i in range(len(nums)):
            nums[i] = rotated[i]
    
    def rotate_as_stack():
        while k:
            p = nums.pop()
            nums.insert(0, p)
            k -= 1
