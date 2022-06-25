class Solution:
    def rec_sum(self, res, prev_stack, prev_sum, candidates, target):
        for i in range(len(candidates)):
            cur_sum = prev_sum
            cur_sum += candidates[i]
            
            if cur_sum > target:
                return
            
            cur_stack = prev_stack.copy()
            cur_stack.append(candidates[i])
            if cur_sum == target:
                res.append(cur_stack)
            else:
                self.rec_sum(res, cur_stack, cur_sum, candidates[i:], target)
            
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.rec_sum(res, [], 0, candidates, target)
        return res
