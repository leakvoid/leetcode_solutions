class Solution:
    def add_range(self, range_start, range_end, res):
        if range_start == range_end:
            res.append(str(range_start))
        else:
            res.append(str(range_start) + "->" + str(range_end))
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return res
        
        range_start = nums[0]
        range_end = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if n == range_end + 1:
                range_end = n
            else:
                self.add_range(range_start, range_end, res)
                range_start = n
                range_end = n
        self.add_range(range_start, range_end, res)
        return res
