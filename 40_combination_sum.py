class Solution:
    memory = {}

    def memorize(self, prev, cand):
        if str(prev) not in self.memory:
            self.memory[str(prev)] = {}
        self.memory[str(prev)][str(cand)] = True

    def already_happened(self, prev, cand):
        if str(prev) in self.memory:
            if str(cand) in self.memory[str(prev)]:
                return True
        return False

    def clear_memory(self):
        self.memory = {}
    
    def rec_sum(self, res, prev_stack, prev_sum, candidates, target):
        if self.already_happened(prev_stack, candidates):
            return
        self.memorize(prev_stack, candidates)
        
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
                status = self.rec_sum(res, cur_stack, cur_sum, candidates[i + 1:], target)
        
    def combinationSum2(self, candidates, target: int):
        self.clear_memory()
        
        candidates.sort()
        res = []
        self.rec_sum(res, [], 0, candidates, target)
        if len(res) < 2:
            return res
        
        res.sort()
        no_dublicates_res = []
        no_dublicates_res.append(res[0])
        for i in range(1, len(res)):
            if res[i - 1] != res[i]:
                no_dublicates_res.append(res[i])
            
        return no_dublicates_res

s = Solution()
print(s.combinationSum2([1,1], 2))
print(s.combinationSum2([1] * 27, 27))
print(s.combinationSum2([1,1], 2))
print(s.combinationSum2([4,4,2,1,4,2,2,1,3], 6))
