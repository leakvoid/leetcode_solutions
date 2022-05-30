
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        
        min_distance = 1000000
        shift = 1
        for i in range(len(nums) - 2):
            n_target = target - nums[i]
            
            s = i + 1
            e = len(nums) - 1
            while s < e:
                c_distance = n_target - nums[s] - nums[e]
                if abs(c_distance) < min_distance:
                    min_distance = abs(c_distance)
                    shift = (-1 if c_distance < 0 else 1)
                
                if c_distance == 0:
                    return target
                elif c_distance < 0:
                    e -= 1
                else:
                    s += 1

        return target - min_distance * shift

s = Solution()
print("[-1,2,1,-4], 1:", s.threeSumClosest([-1,2,1,-4], 1))
print("[-1,0,1,1,55], 3:", s.threeSumClosest([-1,0,1,1,55], 3))
