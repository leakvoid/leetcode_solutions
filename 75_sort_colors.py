class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0,0,0]
        for i in range(len(nums)):
            counter[nums[i]] += 1

        color = 0
        for i in range(len(nums)):
            while counter[color] == 0:
                color += 1
            nums[i] = color
            counter[color] -= 1
        
        #i = 0
        #for color in range(3):
        #    while counter[color] > 0:
        #        nums[i] = color
        #        i += 1
        #        counter[color] -= 1
