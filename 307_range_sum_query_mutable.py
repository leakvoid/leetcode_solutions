import math

class NumArray:

    def __init__(self, nums: List[int]):
        self.dec_factor = int( math.sqrt(len(nums)) )
        self.segment_sum = []
        self.nums = nums
        
        s_sum = 0
        segment_threshold = self.dec_factor
        for i in range(len(nums)):
            if i >= segment_threshold:
                self.segment_sum.append(s_sum)
                s_sum = 0
                segment_threshold += self.dec_factor
            
            s_sum += nums[i]
        
        if segment_threshold >= len(nums):
            self.segment_sum.append(s_sum)

    def update(self, index: int, val: int) -> None:
        pos = index // self.dec_factor
        self.nums[index] = val
        s_sum = 0
        for i in range(pos * self.dec_factor, min((pos + 1) * self.dec_factor, len(self.nums))):
            s_sum += self.nums[i]
        self.segment_sum[pos] = s_sum

    def sumRange(self, left: int, right: int) -> int:
        left_pos = left // self.dec_factor
        right_pos = right // self.dec_factor
        
        res = 0
        if left_pos == right_pos:
            for i in range(left, right + 1):
                res += self.nums[i]
        else:
            for i in range(left, (left_pos + 1) * self.dec_factor):
                res += self.nums[i]

            for i in range(right_pos * self.dec_factor, right + 1):
                res += self.nums[i]

            for i in range(left_pos + 1, right_pos):
                res += self.segment_sum[i]
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

'''
["NumArray","sumRange","update","sumRange","sumRange","update","update","sumRange","sumRange","update","update"]
[[[-28,-39,53,65,11,-56,-65,-39,-43,97]],[5,6],[9,27],[2,3],[6,7],[1,-82],[3,-72],[3,7],[1,8],[5,13],[4,-67]]
["NumArray","sumRange","update","sumRange"]
[[[1,3,5]],[0,2],[1,2],[0,2]]
["NumArray","sumRange","update","sumRange"]
[[[-1]],[0,0],[0,1],[0,0]]
["NumArray","sumRange","sumRange","sumRange","update","update","update","sumRange","update","sumRange","update"]
[[[0,9,5,7,3]],[4,4],[2,4],[3,3],[4,5],[1,7],[0,8],[1,2],[1,9],[4,4],[3,4]]
'''
