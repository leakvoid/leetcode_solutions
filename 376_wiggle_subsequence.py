class Solution:
    def wiggleMaxLength(self, nums: [int]) -> int:
        res = []
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                res.append(1)
            elif nums[i - 1] > nums[i]:
                res.append(-1)
        
        count = len(res) + 1
        for i in range(1, len(res)):
            if res[i - 1] == res[i]:
                count -= 1
        
        return count

s = Solution()
a = [381,157,157,134,431,295]
print( "a: ", a, s.wiggleMaxLength(a) )
# print( s.wiggleMaxLength([372,492,288,399,81,2,320,94,416,469,427,117,265,357,399,456,496,337,355,219,475,295,457,350,490,470,281,127,131,36,430,412,442,174,128,253,1,56,306,295,340,73]) )
